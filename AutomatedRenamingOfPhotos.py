################################################## 
# AUTOMATED RE-NAMING OF PHOTOS                  #  
# Sunday, 2 June 2019                            #
# Written using Python 3.7.2 on Windows 10 Pro   #
#                                                #
# Goal: resize and rename all files in a given   #
# folder (assumed to be images) and save them in #
# a different folder.                            #
################################################## 

import os
from datetime import datetime
#from shutil import copyfile
import random
from PIL import Image

#Set folder containing images as rootdirectory.
root_directory = r"C:\\Users\\Merlijn Kersten\\Pictures\\Photos\soloespresso"
os.chdir(root_directory) #Sets directory

#Steps: 
# 1) find all files in the folder. 
# 2) find their path, and define a new path. 
# 3) find if this new path already exists: if so rename (with random integer to avoid double/triple/... renaming). Generic new name: soloespressoYYYY-MM-DD.jpg ()
# 4) thumbnail image to a width of 800px (height should remain unchanged, therefore max height set to 1,000,000) (images that are smaller will not be changed).
# 5) save image to a sub new folder (which needs to already exist).

for subdir, dirs, files in os.walk(root_directory):
    for file in files:
        old_path = file
        a = os.path.getctime(old_path)                          #creation date (computer)
        b = datetime.fromtimestamp(a).strftime('%Y-%m-%d')      #creation date (human-readable)
        c = "soloespresso" + b +".jpg"                       #new filename
        new_path = os.path.join("Renamed and resized", c)       #new path
        if os.path.isfile(new_path) != True:                    #checks if such a path/file already exists: if not, resizes
            image = Image.open(old_path)
            image.thumbnail((800,100000), Image.ANTIALIAS)      #resize image
            quality_val = 95                                    #highest possible value = 95
            image.save(new_path, quality=quality_val)           #save resized, renamed image
            print("Image #" + file + " is now: " + c)           #prints confirmation
        else:
            new_c = "attention_needed_" + str(random.randint(1,100000)) + "_" + c       #random integer to avoid double-naming (most of the time)
            new_path = os.path.join("Renamed and resized", new_c)
            image = Image.open(old_path)
            image.thumbnail((800,100000), Image.ANTIALIAS)
            quality_val = 95
            image.save(new_path, quality=quality_val)
            print("Attention needed for file" + c)