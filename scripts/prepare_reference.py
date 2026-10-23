#!/usr/bin/env python3
"""Create a non-destructive lightweight PNG reference."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps


def main() -> int:
    parser = argparse.ArgumentParser(description="Prepare a lightweight image-generation reference")
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("--max-long-side", type=int, default=384)
    args = parser.parse_args()
    source = Path(args.input).expanduser().resolve()
    output = Path(args.output).expanduser().resolve()
    if not source.is_file():
        raise SystemExit(f"missing input: {source}")
    if args.max_long_side < 128 or args.max_long_side > 1024:
        raise SystemExit("--max-long-side must be between 128 and 1024")
    if source == output:
        raise SystemExit("input and output must be different files")
    if output.exists():
        raise SystemExit(f"output already exists: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(source) as image:
        reference = ImageOps.exif_transpose(image)
        reference.thumbnail(
            (args.max_long_side, args.max_long_side),
            Image.Resampling.LANCZOS,
        )
        if reference.mode not in {"1", "L", "LA", "P", "RGB", "RGBA", "I", "I;16"}:
            reference = reference.convert("RGB")
        try:
            with output.open("xb") as stream:
                reference.save(stream, format="PNG", optimize=True)
        except FileExistsError as error:
            raise SystemExit(f"output already exists: {output}") from error
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
