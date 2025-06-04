import os

folder = '.'
for filename in os.listdir(folder):
    if filename.endswith('.JPG'):
        new_name = filename[:-4] + '.jpg'
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
        print(f'Renamed: {filename} -> {new_name}')