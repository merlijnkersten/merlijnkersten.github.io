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

root_directory = "C:/Users/Merlijn Kersten/Pictures/soloespresso/Renamed resized"
os.chdir(root_directory)

for subdir, dirs, files in os.walk(root_directory):
    for file in files:
        old_path = file
        new_path = old_path[0:22] + ".jpg"
        check_1 = old_path != new_path              # Are the two paths different? E.g. has the photo already been renamed
        check_2 = os.path.isfile(new_path)          # Does the file path already exist?
        if check_1 and not check_2:                 # Photo has not been renamed yet, and path does not exist yet. 
            os.rename(old_path, new_path)
        elif check_1 and check_2:                   # Path already exists, need to change the name of the photo/a previous photo.
            print(f'Error! File already exists \n {old_path} \n {new_path}')
            input('\nPress any key to quit')
            quit()
        else:                                       # The photo has already been renamed and the path exists: NFA.
            pass