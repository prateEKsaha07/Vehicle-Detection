import os
import shutil
from pathlib import Path

label_dir = Path('dataset/labels/')
source_images = Path('JPEGImages/')
target_images = Path('dataset/images/')

target_images.mkdir(parents=True, exist_ok=True)

moved_count = 0
missing_count = 0

print("Indexing all images...")

image_index = {}

# Index both JPG and PNG
for root, _, files in os.walk(source_images):
    for file in files:
        if file.endswith(('.jpg', '.png')):
            image_index[file] = Path(root) / file

print(f"Indexed {len(image_index)} images")

print("Starting synchronization...")

# Match labels with images
for label_file in label_dir.glob('*.txt'):
    file_stem = label_file.stem

    # Check both formats
    possible_names = [
        f"{file_stem}.jpg",
        f"{file_stem}.png"
    ]

    found = False

    for name in possible_names:
        if name in image_index:
            source_path = image_index[name]
            target_path = target_images / name

            shutil.copy2(source_path, target_path)
            moved_count += 1
            found = True
            break

    if not found:
        print(f"Missing: {file_stem}")
        missing_count += 1

print("---")
print("Sync complete!")
print(f"Images copied: {moved_count}")
print(f"Missing images: {missing_count}")