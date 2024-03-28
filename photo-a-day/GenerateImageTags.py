"""
March 2024

Steps:

Preparation: all new photos in Renamed resized folder, with the correct name.

Find all images in the Renamed resized folder (in Pictures folder).

Sort these photos

For all these photos

    Find their height

    Find their long date (dd month)

    Write the html tags for the website to a file

    Move the photos to the Assets folder (syncs to Github)

Output: photos in the right folder and new text file (on Desktop) with HTML code

"""
import os
from PIL import Image

input_directory = "C:/Users/Merlijn Kersten/Pictures/soloespresso/Renamed resized"

output_directory = "C:/Users/Merlijn Kersten/Documents/code/merlijnkersten.github.io/assets"

output_html_path = "C:/Users/Merlijn Kersten/Desktop/html_text.txt"

files = sorted(os.listdir(input_directory))

html_text_file = open(output_html_path, "w+")

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
    f = os.path.join(input_directory, filename)
    img = Image.open(f)
    height = img.height
    img.close()

    # month is 17:19 of namestring, date is 20:22.
    long_date = filename[20:22] + " " + month_dic[filename[17:19]]

    html_text_file.write(f'			<p><img src="/assets/{filename} style="width:500px;height:{height}px;" loading="lazy" alt="{long_date}" /> </p> \n'),
    html_text_file.write(f'			<p><em> {long_date} </em> </p> \n'),
    html_text_file.write(f'			\n'),


    new_file_path = os.path.join(output_directory, filename)

    os.rename(f, new_file_path)

html_text_file.close()