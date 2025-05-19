"""
January 2025

Input: resized photos (550px width, by Photoscape) with name 
"soloespressoYYYY-MM-DD......jpg" all in the same folder.

Steps:
- Rename photos (leaving "soloespressoYYYY-MM-DD.jpg"),
    - Script stops if two files have the same name.
- Find and soret all renamed photos. For all these photos:
    - Find their height and long date (dd month),
    - Write their html tags for the website to a file
    - Move the photos to the Assets folder (syncs to Github)

Output: photos in the right folder and new text file (on Desktop) with HTML code
"""
import os 
from PIL import Image

input_dir = "C:/Users/Merlijn Kersten/Pictures/soloespresso/Renamed resized"

output_dir = "C:/Users/Merlijn Kersten/Documents/code/merlijnkersten.github.io/assets"
#output_dir = "C:/Users/Merlijn Kersten/Desktop/test output"

output_file = "C:/Users/Merlijn Kersten/Desktop/html_text.txt"


# STEP 1: RENAME FILES

os.chdir(input_dir)

for subdir, dirs, files in os.walk(input_dir):
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


# STEP 2: CREATE HTML-TAGS AND MOVE FILES

files = sorted(os.listdir(input_dir), reverse=True)

html_text_file = open(output_file, "w+")

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

for filename in files:
    f = os.path.join(input_dir, filename)
    img = Image.open(f)
    height = img.height
    img.close()

    # month is 17:19 of namestring, date is 20:22.
    long_date = str(int(filename[20:22])) + " " + month_dic[filename[17:19]]

    html_text_file.write(f'			<p><img src="/assets/{filename}" style="width:550px;height:{height}px;" loading="lazy" alt="{long_date}" /> </p> \n'),
    html_text_file.write(f'			<p><em> {long_date} </em> </p> \n'),
    html_text_file.write(f'			\n'),


    new_file_path = os.path.join(output_dir, filename)

    os.rename(f, new_file_path)

html_text_file.close()