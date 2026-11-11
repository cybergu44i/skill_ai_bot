---
name: reproducible-release-packager
description: Package one already verified version into a local, byte-repeatable tar.gz archive from an approved file allowlist, with a checked member inventory and SHA-256 digests. Use when a developer must hand off a reproducible release artifact. Exclude configuring CI, creating a development environment, changing application behavior, deploying, signing, or publishing.
license: Apache-2.0
---

# Reproducible Release Packager

Deliver a local archive, a sidecar manifest, the exact replay command, and evidence that two clean builds from the same inputs produce identical bytes. A matching digest proves repeatability for the tested inputs and environment, not that the source, binary, or recipient is trustworthy.

## Establish the release contract

1. Read repository instructions and inspect existing changes. Obtain the exact version or source revision, the approved relative-path file list, the already working verification command, the expected runtime/tool versions, and a fixed timestamp in Unix seconds. Do not infer the release contents from a broad directory walk. If an input is missing or contradictory, ask for it and stop dependent packaging.
2. Run the approved verification command locally and record its exit status. If it fails, stop. Do not run downloaded scripts, install dependencies, query secrets, modify production data, or contact a publishing service to manufacture a pass.
3. Inspect the approved files and their origin, including license notices and generated resources. Confirm that each file belongs to the selected revision and license permits distribution. Reject unapproved, temporary, credential, token, private-key, or environment files. A name check alone cannot prove that file contents contain no secrets; review release contents before handoff and use the project's secret scanning policy where available. Do not print secret values.

## Package and verify locally

4. Put one relative path per line in a UTF-8 allowlist. Use only files inside the chosen source tree. The bundled `scripts/pack.py` rejects duplicate, absolute, traversal, symlink, non-file, and suspicious secret-like paths; it has a 100 MiB total input limit. Do not weaken these checks to accommodate an unexpected file. Its output must be outside the source tree.
5. Run `python scripts/pack.py --source SOURCE --files ALLOWLIST --output FIRST.tar.gz --epoch SECONDS` from this skill's folder, substituting local paths and a fixed timestamp. The script sorts members, normalizes owner, mode, and time, fixes the gzip header, and writes `FIRST.tar.gz.manifest.json` with per-member and archive SHA-256 digests. This command performs only local reads and writes.
6. Repeat the command to a second fresh output path with the same source, allowlist, epoch, and tool version. Compare archive SHA-256 and bytes, and compare manifests except for their filenames. If the bytes differ, record the difference and do not label the release reproducible.
7. Inspect archive members using a separate temporary directory and compare their paths and SHA-256 digests to the approved allowlist and manifest. Verify the expected entry point or resource is present. Check explicitly for excluded temporary files and secret-like files. Never extract an untrusted archive into a live project or follow links from one.
8. Report the revision, approved allowlist authority, verification command and result, packaging command, Python version, timestamp, member inventory, archive digest, two-build comparison, and any omissions or environment limits. Keep the package local until separately authorized for release.

## Routing and limits

Use this skill for a local package from already verified inputs. A request for a pull-request check belongs to a CI workflow task. A request to establish a runnable developer environment belongs to a local environment task. A request to adapt dependencies belongs to a migration task. A request to check an existing archive's behavior belongs to a release smoke task. The bundled script is a small deterministic packer for regular files, not a general build system or cryptographic signer; reproducibility across other Python versions, platforms, build tools, or generated binaries requires separate tests.

## Basis and license

Original instructions and script under [Apache-2.0](LICENSE). Conceptual references: [Reproducible Builds archive metadata](https://reproducible-builds.org/docs/archives/), [timestamps](https://reproducible-builds.org/docs/timestamps/), and [checksums](https://reproducible-builds.org/docs/checksums/). No third-party code or instructions were copied.
