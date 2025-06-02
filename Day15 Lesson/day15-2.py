# https://docs.python.org/3/py-modindex.html


# Some Useful modules
# csv , glob , webbrowser , sutil

import glob
import csv
import shutil
import webbrowser


# glob
myfiles = glob.glob("*.py")
print(myfiles)

myfiles2 = glob.glob("day15testing/*.txt")
print(myfiles2)

for filepath in myfiles2:
    with open(filepath, 'r') as file:
        print(file.read().upper())


# CSV
with open("day15testing/example.csv", 'r') as file:
    data = list(csv.reader(file))
print(data)

for row in data:
    print(row)

brand = input("Enter a laptop brand: ")

for row in data:
    if row[0] == brand:
        print(row[1], row[2])
        

# Shutil
# make zip file of a folder
shutil.make_archive("output", "zip", "day15testing")


# Webbrowser
user_search = input("Enter a search term: ").replace(" ", "+")
webbrowser.open("https://www.google.com/search?q=" + user_search)

# just to keep the browser open
input("Press enter to exit")