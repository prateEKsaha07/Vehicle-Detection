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

for root, _, files in os.walk(source_images):
    for file in files:
        if file.endswith('.jpg'):
            image_index[file] = Path(root) / file

print(f"Indexed {len(image_index)} images")

print("Starting synchronization...")

# Match labels with images
for label_file in label_dir.glob('*.txt'):
    file_stem = label_file.stem
    image_name = f"{file_stem}.jpg"

    if image_name in image_index:
        source_path = image_index[image_name]
        target_path = target_images / image_name

        shutil.copy2(source_path, target_path)
        moved_count += 1
    else:
        print(f"Missing: {image_name}")
        missing_count += 1

print("---")
print("Sync complete!")
print(f"Images copied: {moved_count}")
print(f"Missing images: {missing_count}")