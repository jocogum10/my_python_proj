"""
lists all the files in a folder, specified by the format (e.g. pdf, txt, etc..)
from programming python scanning the standard library tree
"""

import sys, os, pprint

dirname = input("Enter the directory: ")
file_type = input("Enter the filetype: ")
prompt = input("Name of file list: ")

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
        if filename.endswith(file_type):
            print('|--->', filename, file=file_list)

file_list.close()         
