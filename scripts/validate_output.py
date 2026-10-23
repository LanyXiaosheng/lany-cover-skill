#!/usr/bin/env python3
"""Validate final dimensions and the selected background mode."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def parse_size(value: str) -> tuple[int, int]:
    try:
        width_text, height_text = value.lower().split("x", 1)
        width, height = int(width_text), int(height_text)
    except (TypeError, ValueError) as error:
        raise argparse.ArgumentTypeError("size must look like 1500x600") from error
    if width <= 0 or height <= 0:
        raise argparse.ArgumentTypeError("size dimensions must be positive")
    return width, height


def corner_luminance(image: Image.Image) -> float:
    width, height = image.size
    patch_width = max(1, round(width * 0.12))
    patch_height = max(1, round(height * 0.12))
    corners = (
        (0, 0),
        (width - patch_width, 0),
        (0, height - patch_height),
        (width - patch_width, height - patch_height),
    )
    values = []
    for left, top in corners:
        patch = image.crop((left, top, left + patch_width, top + patch_height))
        pixels = list(patch.getdata())
        values.append(sum((red + green + blue) / 3 for red, green, blue in pixels) / len(pixels))
    return sum(values) / len(values)


def background_error(args: argparse.Namespace, fraction: float, corner_luma: float) -> str | None:
    if args.background == "dark" and (
        fraction > args.max_light_fraction or corner_luma > args.max_dark_corner_luma
    ):
        return f"FAIL dark background: near-white={fraction:.3f} corner-luma={corner_luma:.1f}"
    if args.background == "light" and (
        fraction < args.min_light_fraction and corner_luma < args.min_light_corner_luma
    ):
        return f"FAIL light background: near-white={fraction:.3f} corner-luma={corner_luma:.1f}"
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a final Lany image")
    parser.add_argument("image")
    parser.add_argument("--size", type=parse_size, required=True)
    parser.add_argument("--background", choices=("dark", "light", "mixed"), default="dark")
    parser.add_argument("--max-light-fraction", type=float, default=0.45)
    parser.add_argument("--min-light-fraction", type=float, default=0.35)
    parser.add_argument("--max-dark-corner-luma", type=float, default=150.0)
    parser.add_argument("--min-light-corner-luma", type=float, default=180.0)
    args = parser.parse_args()
    path = Path(args.image).expanduser().resolve()
    if not path.is_file():
        raise SystemExit(f"missing image: {path}")
    with Image.open(path) as image:
        rgb = image.convert("RGB")
        if rgb.size != args.size:
            print(f"FAIL size={rgb.size[0]}x{rgb.size[1]} expected={args.size[0]}x{args.size[1]}")
            return 2
        sample = rgb.copy()
        sample.thumbnail((256, 256))
        pixels = list(sample.getdata())
        light = sum(1 for red, green, blue in pixels if red >= 235 and green >= 235 and blue >= 235)
        fraction = light / max(len(pixels), 1)
        corner_luma = corner_luminance(sample)
        error = background_error(args, fraction, corner_luma)
        if error:
            print(error)
            return 3
    print(
        f"OK size={args.size[0]}x{args.size[1]} background={args.background} "
        f"near-white-fraction={fraction:.3f} corner-luma={corner_luma:.1f}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
