"""
March 2024

Goal: 
 - Pre-set size of image box,
    - Need to know all heights of images,
 - Lazy-load images,
"""

from PIL import Image
import os

directory = "C:/Users/Merlijn Kersten/Documents/code/merlijnkersten.github.io/assets"

img_height_dic = dict()

for filename in os.listdir(directory):
    # soloespresso
    # 0123456789012
    if filename[:12] == "soloespresso" and filename[-4:].lower() == ".jpg":
        f = os.path.join(directory, filename)
        img = Image.open(f)
        height = img.height
        img_height_dic[filename] = height
        img.close()

file_path = "C:/Users/Merlijn Kersten/Documents/code/merlijnkersten.github.io/soloespresso.html"

# Read in the file
with open(file_path, 'r') as file:
  filedata = file.read()

for key in img_height_dic.keys():
   height = img_height_dic[key]
   old_text = str(key) + '"'
   new_text = old_text + f' style="width:500px;height:{height}px;" loading="lazy"'
   filedata = filedata.replace(old_text, new_text)

quit()

# Write the file out again
with open(file_path, 'w') as file:
  file.write(filedata)
