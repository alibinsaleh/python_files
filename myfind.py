# myfind.py

# find files according to type and a search word (ex. myfind.py <pdf> <search word>)

import os, sys

path = '/Users/alibinsaleh/Downloads/'

if len(sys.argv) == 1 or len(sys.argv) > 3:
    print('hint: myfind.py <file type> <search word>')
else:
    file_type = sys.argv[1]
    search_word = sys.argv[2]

def search(file):
    l = file.split(' ')
    for i in l:
        #print(i.upper())
        if search_word.upper() in i.upper():
            return True
    
    return search_word in l


files = os.listdir(path)
output_file = file_type + '_files.txt'
os.remove(output_file)
for myfile in files:
    if myfile.endswith(file_type):
        if search(myfile):
            with open(file_type+'_files.txt', 'a+') as f:
                f.write(myfile)
            print(myfile)
        


