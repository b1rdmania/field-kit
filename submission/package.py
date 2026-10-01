#!/usr/bin/env python3
"""Build a local submission ZIP from an explicit list of package files."""

import pathlib
import json
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
VERSION = json.loads((ROOT / "plugin.json").read_text())["version"]
OUTPUT = ROOT / "field" / "submission" / f"field-kit-{VERSION}.zip"
FILES = ["plugin.json", "README.md", "LICENSE", "PRIVACY.md", "TERMS.md",
         ".claude-plugin/plugin.json", ".claude-plugin/marketplace.json",
         "submission/portal-copy.md", "submission/test-cases.md", "submission/verification.md"]


def main():
    paths = [ROOT / name for name in FILES]
    for folder in ("skills", "assets"):
        paths.extend(p for p in (ROOT / folder).rglob("*")
                     if p.is_file() and p.suffix in {".md", ".yaml", ".py", ".csv", ".svg", ".png", ".jpg"}
                     and "__pycache__" not in p.parts and not p.is_symlink())
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(paths):
            archive.write(path, path.relative_to(ROOT).as_posix())
    print(f"Built field/submission/{OUTPUT.name} with {len(paths)} files.")
    print("No upload or submission was made.")


if __name__ == "__main__":
    main()
