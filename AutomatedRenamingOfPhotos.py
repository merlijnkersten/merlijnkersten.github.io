# AUTOMATED RE-NAMING OF PHOTOS
# SUNDAY, 2 JUNE

# =============================

# Goal: Need a systematic way to access photos in the /assets repository so
# they can be used on the soloespresso (and eventually nerdonanisland)
# pages. With a few exceptions, there is one photo per day and I therefore
# want to automatically change the name of the pictures to 
# soloespressoYYYY-MM-DD.jpg or something similar. I'll then mannually
# correct the exceptions.

# Input: an 800px-wide image file named 'XXXXX.jpg'
# Output: an 800px-wide image file named 'soloespressoYYYY-MM-DD.jpg'

# Potential issues: 1) some dates have multiple images, will one of them
# be ignored? 

# From https://stackoverflow.com/questions/237079/how-to-get-file-creation-modification-date-times-in-python
# and https://stackoverflow.com/questions/237079/how-to-get-file-creation-modification-date-times-in-python/39501288#39501288
# os.path.getctime() gets creation time (need date) on Windows only.
# needs os and platform

# From https://stackoverflow.com/questions/2491222/how-to-rename-a-file-using-python
# os.rename(old_file, new_file) renames a file. Can use: 
# os.path.join("directory", "name.extensions")

# Alternative (same source):
# from pathlib import Path
# p = Path(some_path)
# p.rename(Path(p.parent, "{}_{}".format(p.stem, 1) + p.suffix))

# https://stackoverflow.com/questions/19501711/how-can-i-convert-os-path-getctime
# For correct date+time
'''
import os
from datetime import datetime

os.chdir(r'C:\\Users\\Merlijn Kersten\\Pictures\\') #Sets directory

old_path = "me.jpg" #location of original file
a = os.path.getctime(old_path) #creation date (computer)
b = datetime.fromtimestamp(a).strftime('%Y-%m-%d') #creation date (human-readable)
c = "soloespresso" + b +".jpg" #correct filename
print(c)
new_path = os.path.join("Renamed", c)
print(new_path)
os.rename(old_path, new_path)
'''
'''
print(True == 1)

if os.path.isfile(new_path) != True:
    print("A file with that name did not yet exist.")
    os.rename(old_path, new_path)
    print("It does now.")
else:
    print("A file with that name already exists.")
    new_c = "attention_needed_" + c
    new_path = os.path.join("Renamed" + new_c)
    print("A file with 'attention needed' + file name was created instead.")
'''