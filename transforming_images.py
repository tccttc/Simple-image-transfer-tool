import os
import re
import shutil

def find_and_move_images(markdown_dir, image_dir):
    for root, _, files in os.walk(markdown_dir):
        for file in files:
            if file.endswith(".md"):
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    content = f.read()

                    # Find image paths like /imgs/?.png
                    image_paths = re.findall(r'imgs/([a-zA-Z0-9_ -]+\.png)', content)
                    print("image_paths: ", image_paths)

                    for image_name in image_paths:
                        # get the src_path and dest_path
                        source_path = os.path.join(image_dir, image_name)
                        dest_path = os.path.join(markdown_dir, 'imgs', image_name)
                        print("src_path: ", source_path)
                        print("dest_path: ", dest_path)

                        if os.path.exists(source_path):
                            # Ensure the 'imgs' directory exists in the markdown directory
                            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                            shutil.move(source_path, dest_path)
                            print(f"Moved {image_name} to {dest_path}")

# Paths to the directories
markdown_directory = r'E:\notes'
image_directory = r'E:\images'

# Call the function to find and move images
find_and_move_images(markdown_directory, image_directory)