import os
from PIL import Image

def ensure_output_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def resize_image(input_path, output_path):
    with Image.open(input_path) as img:
        width, height = img.size
        if width >= height:
            # Landscape: resize width to 960px
            new_width = 960
            new_height = int((960 / width) * height)
        else:
            # Portrait: resize height to 600px
            new_height = 600
            new_width = int((600 / height) * width)
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        resized_img.save(output_path)

def process_images(input_folder, output_folder):
    ensure_output_folder(output_folder)
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            input_path = os.path.join(input_folder, filename)
            name, ext = os.path.splitext(filename)
            output_filename = f"{name}_resized{ext}"
            output_path = os.path.join(output_folder, output_filename)
            resize_image(input_path, output_path)
            print(f"Resized and saved: {output_path}")

if __name__ == "__main__":
    images_folder = "irland-myndir"
    output_folder = "irland"
    process_images(images_folder, output_folder)