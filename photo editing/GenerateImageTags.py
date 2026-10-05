"""
October 2026

Input: resized (550px width) and renamed ("soloespressoYYYY-MM-DD.jpg") 
photos, in the "input_dir" folder. 

Steps:
- Find and sort all renamed photos. For all these photos:
    - Find their height and long date (dd month),
    - Write their html tags for the website to a file
    - Move the photos to the Assets folder (syncs to Github)

Output: photos in the right folder and new text file (on Desktop) with HTML code
"""
import os 
from PIL import Image

input_dir = "/home/rahel/Pictures/soloespresso/Renamed resized/"
output_dir = "/home/rahel/Documents/code/merlijnkersten.github.io/assets"
output_file = "/home/rahel/Desktop/html_text.txt"

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
    print(filename)

    f = os.path.join(input_dir, filename)
    img = Image.open(f)
    height = img.height
    img.close()
    
    # month is 17:19 of namestring, date is 20:22.
    long_date = str(int(filename[20:22])) + " " + month_dic[filename[17:19]]
    html_text_file.write(f'			<p><img src="/assets/{filename}" width="550" height={height} loading="lazy" alt="{long_date}" /> </p> \n'),
    html_text_file.write(f'			<p><em> {long_date} </em> </p> \n'),
    html_text_file.write(f'			\n'),


    new_file_path = os.path.join(output_dir, filename)

    os.rename(f, new_file_path)

html_text_file.close()