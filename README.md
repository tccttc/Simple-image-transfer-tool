First script: `changing_path.py` is used to change the directory as its name implies.
For example, changing the directory from `../_resources/abc.png` to `imgs/abc.png`

Second script: `transforming_images.py`. It scan through a directory called `markdown_directory` and identify all the **image paths** in markdown files, extract it from `image_directory`, then move the **image paths**.
This script is for transferring the images used in markdown files from one folder to another (for some purpose).

Example scenario: you want to move hundreds images from thousands of images in `../_resources` to `imgs/`, given that you have those image paths in your markdown file.
