#!/usr/bin/env python3
"""Image-based visual QA for rendered PPTX slide previews."""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageChops, ImageStat


def bbox_from_background(image: Image.Image, tolerance: int) -> tuple[int, int, int, int] | None:
    rgb = image.convert("RGB")
    corners = [
        rgb.getpixel((0, 0)),
        rgb.getpixel((rgb.width - 1, 0)),
        rgb.getpixel((0, rgb.height - 1)),
        rgb.getpixel((rgb.width - 1, rgb.height - 1)),
    ]
    bg = tuple(sorted(values)[len(values) // 2] for values in zip(*corners))
    bg_img = Image.new("RGB", rgb.size, bg)
    diff = ImageChops.difference(rgb, bg_img).convert("L")
    mask = diff.point(lambda p: 255 if p > tolerance else 0)
    return mask.getbbox()


def luminance_std(image: Image.Image) -> float:
    stat = ImageStat.Stat(image.convert("L"))
    return float(stat.stddev[0])


def analyze_image(path: Path, tolerance: int) -> dict[str, float | str | int | None]:
    image = Image.open(path).convert("RGB")
    bbox = bbox_from_background(image, tolerance)
    std = luminance_std(image)
    if bbox is None:
        return {
            "file": str(path),
            "width": image.width,
            "height": image.height,
            "bbox": None,
            "coverage": 0.0,
            "center_delta_x": 0.0,
            "center_delta_y": 0.0,
            "margin_left": 1.0,
            "margin_right": 1.0,
            "margin_top": 1.0,
            "margin_bottom": 1.0,
            "luminance_std": round(std, 2),
        }

    left, top, right, bottom = bbox
    bbox_w = max(1, right - left)
    bbox_h = max(1, bottom - top)
    coverage = (bbox_w * bbox_h) / (image.width * image.height)
    center_delta_x = ((left + right) / 2 - image.width / 2) / image.width
    center_delta_y = ((top + bottom) / 2 - image.height / 2) / image.height
    return {
        "file": str(path),
        "width": image.width,
        "height": image.height,
        "bbox": f"{left},{top},{right},{bottom}",
        "coverage": round(coverage, 3),
        "center_delta_x": round(center_delta_x, 3),
        "center_delta_y": round(center_delta_y, 3),
        "margin_left": round(left / image.width, 3),
        "margin_right": round((image.width - right) / image.width, 3),
        "margin_top": round(top / image.height, 3),
        "margin_bottom": round((image.height - bottom) / image.height, 3),
        "luminance_std": round(std, 2),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run image-based visual QA on rendered slide PNGs.")
    parser.add_argument("preview_dir", type=Path, help="Directory containing slide_*.png previews.")
    parser.add_argument("--tolerance", type=int, default=18, help="background-difference threshold")
    parser.add_argument("--min-coverage", type=float, default=0.36)
    parser.add_argument("--max-center-delta", type=float, default=0.13)
    parser.add_argument("--max-margin", type=float, default=0.28)
    parser.add_argument("--warn-only", action="store_true")
    args = parser.parse_args()

    paths = sorted(args.preview_dir.glob("slide_*.png"))
    if not paths:
        raise SystemExit(f"No slide_*.png files found in {args.preview_dir}")

    warnings = []
    for idx, path in enumerate(paths, 1):
        info = analyze_image(path, args.tolerance)
        reasons = []
        if float(info["coverage"]) < args.min_coverage:
            reasons.append(f"low coverage {info['coverage']}")
        if abs(float(info["center_delta_x"])) > args.max_center_delta:
            reasons.append(f"x-center drift {info['center_delta_x']}")
        if abs(float(info["center_delta_y"])) > args.max_center_delta:
            reasons.append(f"y-center drift {info['center_delta_y']}")
        for key in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
            if float(info[key]) > args.max_margin:
                reasons.append(f"{key} {info[key]}")
        if float(info["luminance_std"]) < 7:
            reasons.append(f"very low contrast/std {info['luminance_std']}")
        if reasons:
            warnings.append((idx, path.name, reasons, info))

    print(f"slides_checked: {len(paths)}")
    print(f"visual_warnings: {len(warnings)}")
    for slide_no, name, reasons, info in warnings[:40]:
        print(f"  P{slide_no:02d} {name}: {'; '.join(reasons)}")
        print(
            "    "
            f"coverage={info['coverage']} center=({info['center_delta_x']},{info['center_delta_y']}) "
            f"margins=({info['margin_left']},{info['margin_right']},{info['margin_top']},{info['margin_bottom']}) "
            f"std={info['luminance_std']}"
        )

    return 0 if args.warn_only or not warnings else 1


if __name__ == "__main__":
    raise SystemExit(main())
