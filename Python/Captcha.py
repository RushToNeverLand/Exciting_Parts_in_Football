# coding=utf-8
from PIL import Image, ImageOps
import subprocess, sys, os


def capcha1(infile, start, end, step):
    if os.path.exists("data"):
        pass
    else:
        os.mkdir("data")
    for i in range(start, end, step):
        subprocess.call(
            'ffmpeg.exe  -ss ' + str(i) + ' -i "' + infile + '" -y -f  image2 -vframes 1  data/test' + str(i) + '.jpg')
        im = Image.open("./data/test" + str(i) + ".jpg")
        region = im.crop((261, 42, 289, 68))
        region = ImageOps.invert(region)
        region = region.point(lambda x: 0 if x < 170 else 255)
        region = region.resize((28, 27))
        region = region.convert('1')
        region.save("./data/Lcrop" + str(i).zfill(5) + ".jpg", dpi=(300, 300))
        region2 = im.crop((295, 41, 323, 68))
        region2 = ImageOps.invert(region2)
        region2 = region2.point(lambda x: 0 if x < 170 else 255)
        region2 = region2.resize((28, 27))
        region2 = region2.convert('1')
        region2.save("./data/Rcrop" + str(i).zfill(5) + ".jpg", dpi=(300, 300))

# im = Image.open("F:/162.jpg")
# region = im.crop((261, 42, 289, 68))
# region.save("234.jpg")