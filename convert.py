import xml.etree.ElementTree as ET
import os

# Configuration
input_dir = 'annotations/'
output_dir = 'dataset/labels'

class_mapping = {
    'car': 0,
    'motorcycle': 1,
    'truck': 2
}

os.makedirs(output_dir, exist_ok=True)

def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    return (x * dw, y * dh, w * dw, h * dh)

for root_dir, _, files in os.walk(input_dir):
    for file in files:
        if not file.endswith('.xml'):
            continue

        xml_path = os.path.join(root_dir, file)

        tree = ET.parse(xml_path)
        root = tree.getroot()

        # Get image size
        size = root.find('size')
        if size is None:
            continue

        width = int(size.find('width').text)
        height = int(size.find('height').text)

        yolo_data = []

        for obj in root.findall('object'):
            cls_name = obj.find('name').text

            if cls_name in class_mapping:
                cls_id = class_mapping[cls_name]

                xml_box = obj.find('bndbox')
                b = (
                    float(xml_box.find('xmin').text),
                    float(xml_box.find('xmax').text),
                    float(xml_box.find('ymin').text),
                    float(xml_box.find('ymax').text)
                )

                bb = convert((width, height), b)

                # Skip invalid boxes
                if bb[2] <= 0 or bb[3] <= 0:
                    continue

                yolo_data.append(
                    f"{cls_id} {' '.join([f'{a:.6f}' for a in bb])}"
                )

        # Save only if valid objects exist
        if yolo_data:
            out_file = os.path.join(output_dir, file.replace('.xml', '.txt'))
            with open(out_file, 'w') as f:
                f.write('\n'.join(yolo_data))

print(f"Conversion complete. Files saved to {output_dir}")