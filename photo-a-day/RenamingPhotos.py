################################################## 
# AUTOMATED RE-NAMING OF PHOTOS                  #  
# Sunday, 2 June 2019                            #
# Written using Python 3.7.2 on Windows 10 Pro   #
#                                                #
################################################## 

# Change name of files after PhotoScape X Pro conversion (width to max 800px, name: soloespressoYYYY-MM-DD asdfg.jpg)
#                                                                                   00000000001111111111122222...
#                                                                                   01234567890123456789012345...
#                                                                                                         ^CHOP AT 22
#                                                                                   soloespressoYYYY-MM-DD.jpg
# Then save image with new name in same folder (deleting previous file). If name already exists, add "ATTENTION" plus a random integer <1,000,000.
# Returns number of images that need attention.
# Alternative to "RenamingResizingPhotos.py"; this can be used until aforementioned is ready.
import os
from datetime import datetime
import random

root_directory = "C:/Users/Merlijn Kersten/Pictures/soloespresso/Renamed resized"
os.chdir(root_directory)

i = 0

for subdir, dirs, files in os.walk(root_directory):
    for file in files:
        old_path = file
        new_path = old_path[0:22] + ".jpg"
        if os.path.isfile(new_path) != True:
            os.rename(old_path, new_path)
        else:
            new_path = "ATTENTION_" + str(random.randint(1,100000)) + "_" + new_path
            os.rename(old_path, new_path)
            i += 1

print("Attention need for " + str(i) + " files.")

