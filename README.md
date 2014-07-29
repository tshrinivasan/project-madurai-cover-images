How to create cover images for all the ebooks in ProjectMadurai.org ?
=====================================================================

1. Get all the book names,author name from 
http://www.projectmadurai.org/pmworks.html

2. Copy them into a LibreOffice Calc spreadsheet.

3. Add serial number in a new front column.

4. Export as CSV file. Put $ as the delimeter.

5. Run the file parser.py

python parser.py

It will extract the book name, author and generate html files, with a background image for the cover art.


6. Download wkhtmltopdf from http://wkhtmltopdf.org/downloads.html

The websites gives latest binary with QT binding.
The one that comes with ubuntu in default is very old.

Download it from the site and install it.

It gives two utilities. 1. wkhtmltopdf  2. wkhtmltoimage

We use wkhtmltoimage to convert the html files into images.


Example : 

wkhtmltoimage --height 640 --width 429  001.html 001.jpg


7. Now, using a small shell script, we can convert all the html files into images.

for i in *.html; do wkhtmltoimage --height 640 --width 429 $i `basename $i .html`.jpg; done


Thats all.
We get all the images.


Background Image source: http://pixabay.com/en/grey-background-texture-template-370125/
License     Public Domain CC0


Uploaded all the generated cover images here:
https://picasaweb.google.com/tshrinivasan/ProjectMaduraiCoverImages?noredirect=1
