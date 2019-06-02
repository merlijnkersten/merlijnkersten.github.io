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

print("Try 1")

import os
path = os.path.join("C:", "Users", "Merlijn Kersten", "Pictures", "me.jpg")
a = os.path.getctime(r"C:\Users\Merlijn Kersten\Pictures\me.jpg")
print(a)