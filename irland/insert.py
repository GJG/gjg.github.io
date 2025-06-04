import os
import re

html_file = "index.html"
image_extensions = (".JPG",".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff")
image_files = [f for f in os.listdir('.') if f.endswith(image_extensions) and "_resized" in f]

# Read the current HTML
with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

# Replace the images array in the HTML
pattern = r"(const images = \[)[\s\S]*?(\];)"
replacement = f'\\1\n    ' + ',\n    '.join(f'"{img}"' for img in image_files) + '\n\\2'
new_html = re.sub(pattern, replacement, html)

# Write back the updated HTML
with open(html_file, "w", encoding="utf-8") as f:
    f.write(new_html)

print(f"Updated {html_file} with {len(image_files)} images.")