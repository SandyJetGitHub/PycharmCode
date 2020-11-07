import sys
import os
from PIL import Image

from_folder = sys.argv[1]
to_folder = sys.argv[2]


def check_folder_exist(path):
    is_exist = os.path.exists(path)
    return is_exist


def create_folder(path):
    os.mkdir(path)
    return True


def extract_list_of_files(path):
    image_file_path_list_tmp = []
    for files in os.listdir(path):
        image_file_path = os.path.join(path, files)
        image_file_path_list_tmp.append(image_file_path)
    return image_file_path_list_tmp


def convert_to_png(image_path_list, image_folder):
    for image_file in image_path_list:
        img = Image.open(image_file)
        file_name = os.path.basename(image_file)
        file_name = file_name.replace('jpg', 'png')
        file_name = os.path.join(image_folder, file_name)
        print(file_name)
        img.save(file_name, 'png')


folder_exist = check_folder_exist(from_folder)
if not folder_exist:
    print('No image folder exist')
else:
    print(f'{from_folder} exists')

folder_exist = check_folder_exist(to_folder)
if not folder_exist:
    print(f'{to_folder} does not exist. Hence, creating new folder')
    create_folder(to_folder)
else:
    print(f'{to_folder} exists')

image_file_path_list = extract_list_of_files(from_folder)
print(image_file_path_list)

convert_to_png(image_file_path_list, to_folder)
