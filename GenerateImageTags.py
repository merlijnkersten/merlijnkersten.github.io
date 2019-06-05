# GENERATE HTML IMAGE TAGS
# June 2019

# GOAL
# Generate HTML image tags for nerdonanisland and soloespresso. They should look like:
#
#       <p><img src='/assets/soloespressoYYYY-MM-DD.jpg' alt='DD mmmmmm' /></p>
#       <p><em>DD mmmmm</em> </p>
# Note: MM en DD in file name need to be double digit.

# Issues: there are no (non-error) safeguards for wrong inputs!
 
# Change directory to Desktop.
import os
os.chdir(r"C:\\Users\\Merlijn Kersten\\Desktop")

# Ask for which dates (inclusive) tags need to be generated.
print(" ")
print("HTML IMAGE TAG GENERATOR")
print("")
print(        "                         YYYY-MM-DD")
start = input("Start date (YYYY-MM-DD)? ")
end = input("End date (YYYY-MM-DD?    ")

# Seperate dates into years/months/days and turn into strings.
start_year = int(start[0:4])
start_month = int(start[5:7])
start_day = int(start[8:])

end_year = int(end[0:4])
end_month = int(end[5:7])
end_day = int(end[8:])

current_year = int(start_year)
current_month = int(start_month)
current_day = int(start_day)

# Turn single diggit days and months into double digits: 5 --> '05' (needed for filename).
def double_Digits(number):
    if len(str(number)) == 1:
        number = "0" + str(number)
    else:
        number = str(number)
    return number

# Number of days per month (leap years dealt with later), names corresponding to numbers of month.
month_lengths = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
month_names = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}

# Create a writeable textfile.
html_text_file = open("htmltext.txt", "w+")

# While the current date is not after the end date, create an image tag for that date. 
while ((current_year == end_year and current_month == end_month) and current_day > end_day) == False:
    # Special case: when the current year is a leap-year, set the month-length for February to the correct number of days, 29. Else is there to reset to 28 just in case.
    if current_year%4 == 0: 
        month_lengths[2] = 29
    else:
        month_lengths[2] = 28
    # HTML tags. Line breaks are for (human) readability.
    html_text_file.write('<p><img src="/assets/soloespresso' + str(current_year) + '-' +  double_Digits(current_month) + '-' + double_Digits(current_day) + '.jpg" alt="'+ str(current_day) + " " + month_names[current_month] +'" /></p>' + '\n'),
    html_text_file.write("<p><em> " + str(current_day) + " " + month_names[current_month] +  " </em> </p>" + '\n'),
    html_text_file.write('\n'),
    
    # If the end of the year is reached, change current date to the first day of the next year (YYYY-31-12 --> YYYY+1-01-01). 
    if current_day == month_lengths[current_month] and current_month == 12:
        current_month = 1
        current_day = 1
        current_year += 1
    # If the end of the month is reached, change current date to the first day of the next month (YYYY-MM-31 --> YYYY-MM+1-01).
    elif current_day == month_lengths[current_month]:
        current_month += 1
        current_day = 1
    # Else change to the next day.
    else:
        current_day += 1

# Close the text file. Print statements that it is ready.
html_text_file.close()
print(" ")
print("File should be on your deskptop.")
print("Captions, if any, should be added manually.")
print(" ")






