import sys, os
from PIL import Image, ImageOps

if len(sys.argv) == 3:
    extention = ['.jpg','.jpeg','.png']
    ext1 = os.path.splitext(sys.argv[1])
    ext2 = os.path.splitext(sys.argv[2])

    if ext1[1].lower() == ext2[1].lower() and ext1[1] in extention:
        try:
            user_image = Image.open(sys.argv[1],'r')
        except FileNotFoundError:
            sys.exit('Input does not exist')

        shirt = Image.open('shirt.png')
        size = shirt.size
        user_image = ImageOps.fit(user_image, size)
        user_image.paste(shirt, shirt)
        user_image.save(sys.argv[2])
    elif ext2[1].lower() not in extention:
        sys.exit('Invalid output')
    elif ext1[1].lower() != ext2[1].lower() and ext1[1].lower() in extention:
        sys.exit('Input and output have different extensions')
elif len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
