#!/usr/bin/env python3
import sys
from pathlib import Path
import numpy as np
from PIL import Image

def gray_world(img: Image.Image) -> Image.Image:
    arr = np.asarray(img.convert("RGB")).astype(np.float32)
    means = arr.reshape(-1, 3).mean(axis=0)
    gain = means.mean() / means          # scale each channel toward the common mean
    arr *= gain
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))

src = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
out = src / "corrected"
out.mkdir(exist_ok=True)

for f in src.iterdir():
    if f.suffix.lower() in {".jpg", ".jpeg", ".png", ".tif", ".tiff"}:
        gray_world(Image.open(f)).save(out / f.name, quality=95)
        print("Processed:", f.name)
