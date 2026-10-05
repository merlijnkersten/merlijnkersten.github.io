# Editing steps
As of: October 2026.

Because I always forget how to do it.

1. Edit photos in Rawtherapee, 
2. Select one photo per day and copy it to "Pictures/soloespresso" folder in D,
3. Copy the photos again, to the folder "Pictures/soloespresso/todo". These are the files that will be renamed and resized, the files in the main folder are meant as a full-sized archive.
4. Rename photos in Digikam: "Edit" -> "Rename" (soloespresso[date:"yyyy-MM-dd"]).
5. Check that the photos are renamed correctly. 
6. Batch apply the "550width" profile in Rawtherapee:
    - Right-click, "Processing file operations" -> "Apply" -> "My profiles -> "550width"
    - Right-click, "Put to queue"
    - Options: "Save to folder": "Renamed resized", uncheck "Save processing parameters with image".
    - Run queue
7. Check that the photos are saved correctly. 
8. Run the "GenerateImageTags.py" script.
9. Check that the images got moved correctly into the "Assets" folder.
10. Copy the HTML tags into the "soloespresso.html" file, and write comments (and `<pre> cheat - DD Month </pre> `when necessary),
11. In the terminal:
     - ` cd Documents/code/merlijnkersten.github.io`
     - `git status` and check files
     - `git add .`
     - `git commit . -m 'First date-last date'`
     - `git push`

Done!