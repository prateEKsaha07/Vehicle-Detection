from pathlib import Path

label_dir = Path('dataset/labels/')
image_dir = Path('dataset/images/')

removed_count = 0

for label_file in label_dir.glob('*.txt'):
    file_stem = label_file.stem

    # Check both jpg and png
    img_jpg = image_dir / f"{file_stem}.jpg"
    img_png = image_dir / f"{file_stem}.png"

    if not img_jpg.exists() and not img_png.exists():
        label_file.unlink()  # delete file
        removed_count += 1

print(f"Removed {removed_count} orphan labels")