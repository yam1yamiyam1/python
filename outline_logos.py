import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

try:
    import numpy as np
    from PIL import Image
    from scipy.ndimage import binary_dilation
except ImportError:
    print("[ERROR] Missing libraries. Run this first:")
    print("  C:\\Python314\\python.exe -m pip install Pillow numpy scipy")
    sys.exit(1)

input_dir = "cloud_drip_logos"
output_dir = "cloud_drip_logos_outlined"
folders = ["NBA", "NFL", "MLB", "NHL", "Brands"]

OUTLINE_SIZE = 18  # px — change this for thicker/thinner outline
PADDING = OUTLINE_SIZE + 4

for folder in folders:
    os.makedirs(f"{output_dir}/{folder}", exist_ok=True)

# Circular structuring element for dilation
r = OUTLINE_SIZE
y_idx, x_idx = np.ogrid[-r : r + 1, -r : r + 1]
STRUCT = x_idx**2 + y_idx**2 <= r**2


def add_outline(img):
    img = img.convert("RGBA")
    w, h = img.size
    new_w = w + PADDING * 2
    new_h = h + PADDING * 2

    # Place alpha on padded canvas
    alpha = np.array(img)[:, :, 3]
    padded_alpha = np.zeros((new_h, new_w), dtype=np.uint8)
    padded_alpha[PADDING : PADDING + h, PADDING : PADDING + w] = alpha

    # Dilate alpha to get outline area
    binary = padded_alpha > 128
    dilated = binary_dilation(binary, structure=STRUCT)

    # White outline layer
    outline = np.zeros((new_h, new_w, 4), dtype=np.uint8)
    outline[dilated] = [255, 255, 255, 255]

    # Original image on padded canvas
    padded = np.zeros((new_h, new_w, 4), dtype=np.uint8)
    padded[PADDING : PADDING + h, PADDING : PADDING + w] = np.array(img)

    # Composite original over outline
    a = padded[:, :, 3:4] / 255.0
    result = (padded * a + outline * (1 - a)).astype(np.uint8)

    return Image.fromarray(result, "RGBA")


total_ok = 0
total_fail = 0

for folder in folders:
    in_folder = f"{input_dir}/{folder}"
    out_folder = f"{output_dir}/{folder}"

    if not os.path.exists(in_folder):
        print(f"\n[SKIP] {folder} -- folder not found")
        continue

    files = [f for f in os.listdir(in_folder) if f.lower().endswith(".png")]
    print(f"\n[{folder}] {len(files)} logos...")

    for filename in files:
        try:
            img = Image.open(f"{in_folder}/{filename}")
            outlined = add_outline(img)
            outlined.save(f"{out_folder}/{filename}", "PNG")
            print(f"  [OK]    {filename}")
            total_ok += 1
        except Exception as e:
            print(f"  [FAIL]  {filename} -- {e}")
            total_fail += 1

print(f"\n[DONE] {total_ok} outlined, {total_fail} failed.")
print(f"Check '{output_dir}' folder.")
