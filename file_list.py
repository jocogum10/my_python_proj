"""
lists all the files in a folder, specified by the format (e.g. pdf, txt, etc..)
from programming python scanning the standard library tree
"""

import sys, os, pprint

dirname = input("Enter the directory: ")
file_type = input("Enter the filetype: ")
prompt = input("Name of file list: ")

file_type_lower = file_type.lower()
file_type_upper = file_type.upper()
file_list = open("{0}.txt".format(prompt), 'w')
visited = {}
my_file = []
for (thisDir, subsHere, filesHere) in os.walk(dirname):
    print('Directory', thisDir, file=file_list)
    thisDir = os.path.normpath(thisDir)
    fixcase = os.path.normcase(thisDir)
    if fixcase in visited:
        continue
    else:
        visited[fixcase] = True
    for filename in filesHere:
        if filename.endswith(file_type_lower) or filename.endswith(file_type_upper):
            try:
                print('|--->', filename, file=file_list)
                my_file.append(filename)
            except UnicodeEncodeError:
                pass
print("###################################################################", file=file_list)
print("\n", file=file_list)
my_list = sorted(my_file)
number_of_files = len(my_list)
print("Number of files found:", file=file_list)
print(number_of_files, file=file_list)
for file in my_list:
    print(file, file=file_list)
    
file_list.close()         
