import os
import random


def split_and_format_images(folder_path):
    all_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    image_files = [file for file in all_files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    random.shuffle(image_files)

    midpoint = len(image_files) // 2
    first_half, second_half = image_files[:midpoint], image_files[midpoint:]

    def format_filenames(names):
        return [f'<img src="{{{{ url_for(\'static\', filename=\'{name}\') }}}}" loading="lazy"/>' for name in names]

    first_half_formatted = format_filenames(first_half)
    second_half_formatted = format_filenames(second_half)

    with open('first_half.txt', 'w') as f1, open('second_half.txt', 'w') as f2:
        f1.write('\n'.join(first_half_formatted))
        f2.write('\n'.join(second_half_formatted))



folder_path = r""
split_and_format_images(folder_path)


