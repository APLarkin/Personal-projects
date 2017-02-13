#This was made for the purpose of easing the modifying of the game Europa Universalis IV, which previously required significant effort in going through and editing thousands of files by hand.

from glob import *
import os
import shutil


path = input("Please enter the location of your mod's province history files (use double backslashes): ")
path = path+"\\*.txt"
whatever = input("What are you looking for? ")
replacement = input("What do you want to replace it with? (If you're looking to add a line in the same place, e.g. if you're adding a new techgroup, enter BOTH the original AND the new line, separated by the newline character (\\n) with NO spaces between them)")


for file in glob(path):
    with open(file, 'r') as infile:
        with open('./newfile.txt.tmp', 'w') as outfile:
            lines = [line.strip() for line in infile]
            for i in range(len(lines)):
                if lines[i] == whatever:
                    lines[i] = replacement
                    continue
            for i in range(len(lines)):
                outfile.write(lines[i]+'\n')
            outfile.close()
            shutil.copyfile('./newfile.txt.tmp', file)
    infile.close()
