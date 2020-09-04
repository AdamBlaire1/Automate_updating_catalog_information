
#!/usr/bin/env python3
from PIL import Image
import os
path = (r"images/")
for file in os.listdir(path):
    print(file)
    if file.endswith(".tiff"):
        im = Image.open(path + file)
        print(im)
        print(path + file.split(".tiff")[0]+'.jpeg')
        im.convert('RGB').resize((600,400)).save(path + file.split(".tiff")[0]+'.jpeg')
        im.close()













