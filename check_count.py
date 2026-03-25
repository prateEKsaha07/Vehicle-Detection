from pathlib import Path

image_dir = Path('dataset/images/')
label_dir = Path('dataset/labels/')

num_images = len(list(image_dir.glob('*')))
num_labels = len(list(label_dir.glob('*.txt')))

print(f"Total Images: {num_images}")
print(f"Total Labels: {num_labels}")