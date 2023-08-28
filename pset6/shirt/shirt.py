# https://cs50.harvard.edu/python/2022/psets/6/shirt/

import sys, os
from PIL import Image, ImageOps

def main():
    try:
        get_shirt(get_arguments())
    except FileNotFoundError:
        exit(f"Input does not exist")

def get_arguments():
    if len(sys.argv) < 3:
        exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        exit("Too many command-line arguments")
    else:
        ext_list = [".jpg", ".jpeg", ".png"]
        ext1 = os.path.splitext(sys.argv[1])[1].lower()
        ext2 = os.path.splitext(sys.argv[2])[1].lower()
        if  ext1 not in ext_list or ext2 not in ext_list:
            exit("Invalid output")
        elif ext1 != ext2:
            exit("Input and output have different extensions")
        else:
            return sys.argv

def get_shirt(files):
    input_img = Image.open(files[1])
    shirt = Image.open("shirt.png")
    shirt_size = shirt.size
    input_resized = ImageOps.fit(input_img, shirt_size)
    input_resized.paste(shirt, mask=shirt)
    input_resized.save(files[2])


if __name__ == "__main__":
    main()