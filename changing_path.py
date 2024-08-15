import os
import re

def update_image_paths_in_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # String you would like to substitute. Change the regex expression if needed.
    updated_content = re.sub(r'\.\./_resources/([a-zA-Z0-9_]+\.png)', r'imgs/\1', content)
    print(updated_content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

def update_image_paths_in_markdown_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                print(file_path)
                update_image_paths_in_markdown_file(file_path)

# Path to the directory containing markdown files
directory_path = r"E:\notes"

# Call the function to update image paths in markdown files within the directory
update_image_paths_in_markdown_files(directory_path)