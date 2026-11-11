"""Build a bounded deterministic local release archive from an explicit allowlist."""

import argparse
import gzip
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import sys
import tarfile

MAX_BYTES = 100 * 1024 * 1024
SECRET_PART = re.compile(r"(^|[._-])(env|secret|secrets|token|tokens|credential|credentials|private[-_]?key|id_rsa)([._-]|$)", re.I)


def approved_paths(source: Path, allowlist: Path) -> list[tuple[str, bytes, int]]:
    if not source.is_dir() or source.is_symlink():
        raise ValueError("source must be a real directory")
    lines = allowlist.read_text(encoding="utf-8").splitlines()
    if not lines or any(not x or x != x.strip() for x in lines):
        raise ValueError("allowlist needs nonblank, unpadded paths")
    paths = []
    seen = set()
    total = 0
    for name in lines:
        p = PurePosixPath(name)
        if p.is_absolute() or name.startswith("./") or "\\" in name or any(x in ("", ".", "..") for x in name.split("/")):
            raise ValueError(f"unsafe member path: {name}")
        if name in seen:
            raise ValueError(f"duplicate member: {name}")
        seen.add(name)
        if any(SECRET_PART.search(part) for part in p.parts):
            raise ValueError(f"secret-like member path: {name}")
        path = source.joinpath(*p.parts)
        if any(parent.is_symlink() for parent in (path, *path.parents) if parent == source or source in parent.parents):
            raise ValueError(f"symlink member: {name}")
        if not path.is_file():
            raise ValueError(f"missing or non-file member: {name}")
        size = path.stat().st_size
        total += size
        if total > MAX_BYTES:
            raise ValueError("input exceeds 100 MiB limit")
        data = path.read_bytes()
        if len(data) != size:
            raise ValueError(f"member changed while reading: {name}")
        mode = 0o755 if path.stat().st_mode & 0o111 else 0o644
        paths.append((name, data, mode))
    return sorted(paths)


def pack(source: Path, allowlist: Path, output: Path, epoch: int) -> dict:
    if source.is_symlink():
        raise ValueError("source must not be a symlink")
    source = source.resolve()
    if epoch < 0:
        raise ValueError("epoch must be nonnegative")
    if output.resolve().is_relative_to(source):
        raise ValueError("output must be outside source")
    if output.exists() or output.with_name(output.name + ".manifest.json").exists():
        raise ValueError("output or manifest already exists")
    entries = approved_paths(source, allowlist)
    if not entries:
        raise ValueError("allowlist has no files")
    if not output.parent.is_dir():
        raise ValueError("output parent does not exist")
    try:
        with output.open("xb") as raw:
            with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as gz:
                with tarfile.open(fileobj=gz, mode="w", format=tarfile.USTAR_FORMAT) as tar:
                    for name, data, mode in entries:
                        info = tarfile.TarInfo(name)
                        info.size = len(data)
                        info.mtime = epoch
                        info.uid = info.gid = 0
                        info.uname = info.gname = ""
                        info.mode = mode
                        tar.addfile(info, io.BytesIO(data))
        manifest = {
            "epoch": epoch,
            "files": [{"path": n, "size": len(d), "sha256": hashlib.sha256(d).hexdigest()} for n, d, _ in entries],
            "archive_sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
        }
        output.with_name(output.name + ".manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        return manifest
    except Exception:
        output.unlink(missing_ok=True)
        output.with_name(output.name + ".manifest.json").unlink(missing_ok=True)
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--files", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--epoch", type=int, required=True)
    args = parser.parse_args()
    try:
        result = pack(args.source, args.files, args.output, args.epoch)
    except (OSError, ValueError, tarfile.TarError) as exc:
        print(f"packaging refused: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({"archive_sha256": result["archive_sha256"], "members": len(result["files"])}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
