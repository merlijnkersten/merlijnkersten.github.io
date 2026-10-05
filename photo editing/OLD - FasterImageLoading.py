"""
March 2024

Goal: 
 - Pre-set size of image box,
    - Need to know all heights of images,
 - Lazy-load images,
"""

from PIL import Image
import os
import re

directory = "C:/Users/Merlijn Kersten/Documents/code/merlijnkersten.github.io/assets"

img_height_dic = dict()

img_width_dic = dict()

for filename in os.listdir(directory):
    # soloespresso
    # 0123456789012
    if filename[:12] == "soloespresso" and filename[-4:].lower() == ".jpg":
        f = os.path.join(directory, filename)
        img = Image.open(f)
        height = img.height
        img_height_dic[filename] = height
        width = img.width
        if width > 550:
           img_width_dic[filename] = (width, height)
        img.close()

print(img_width_dic)

quit()

file_path = "C:/Users/Merlijn Kersten/Documents/code/merlijnkersten.github.io/soloespresso.html"

#print(img_height_dic)

month_dic = {
    '01' : 'January',
    '02' : 'February',
    '03' : 'March',
    '04' : 'April',
    '05' : 'May',
    '06' : 'June',
    '07' : 'July',
    '08' : 'August',
    '09' : 'September',
    '10' : 'October',
    '11' : 'November',
    '12' : 'December'
}

# Read in the file
with open(file_path, 'r') as file:
  filedata = file.read()

for key in img_height_dic.keys():
   height = img_height_dic[key]
   old_text = "'/assets/" + str(key) +  "'/></p" 
   month=key[17:19]
   day=str(int(key[20:22]))
   date = day + " " + month_dic[month]
   new_text = '"/assets/' + str(key) + f'" style="width:550px;height:{height}px;" loading="lazy" alt="{date}" /></p'
   filedata = filedata.replace(old_text, new_text)
   

'''
for key in img_height_dic.keys():
   height = img_height_dic[key]
   old_text = str(key) +  '" style="width:550px;height:(\d+)px;"' 
   new_text = str(key) + f'" style="width:550px;height:{height}px;"'
   filedata = re.sub(old_text, new_text, filedata, flags=re.M)
'''
# Write the file out again
quit()

output_path = "C:/Users/Merlijn Kersten/Desktop/new.html"

with open(file_path, 'w') as file:
  file.write(filedata)
