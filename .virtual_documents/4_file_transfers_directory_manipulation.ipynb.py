# 4 File transfer, references and directory manipuation

# os module: used for managing and locating files and folders 
# can use relative and absolute file names

# shelve module: to save files that are non-text, like dictionary or lists
# shutil module: shell utility, copy and move files 
# send2trash module: to make sure that its not

# using a directory tree os.walk
# Image file sorting template



# os library is used for managing file paths, to locate files

import os

# this is to join strings to create the filepath to locate file
os.path.join('folder 1', 'folder 2', 'file.png')

# get current file path ( current working directory)
os.getcwd()

# change directory
os.chdir(r'C:\Users\User\Desktop\automate')

# relative and absolute path name

# .\ this directory (rrelative reference to current folder)
# ..\ parent folder (relative reference to current folder))

# absolute reference
# c:\\folder1\folder2\spam.png

# sed to reference parent ..\ goes back 2 parent levels
os.path.abspath('..\\..\\spam.png')

# get file directory
os.path.dirname('c:\\folder1\\folder2\\spam.png')

# get file name
os.path.basename('c:\\folder1\\folder2\\spam.png')

# check if file exist
os.path.exists('c:\\folder1\\folder2\\spam.png')

# returns the items in that folder
os.listdir(r'c:\Users\User\Desktop\automate')



# create new folder os.makedirs()

os.makedirs(r'C:\Users\User\Desktop\automate\spare')


# to check if file name exist 
import os
filename = 'dictionary.ipynb'
os.path.isfile(os.path.join(r'c:\Users\User\Desktop\automate',filename))


# a loop to count the size of files in a folder

totalSize = 0
for filename in os.listdir(r'c:\Users\User\Desktop\automate'):

    # dount size of files that are not file names in the folder
    if not os.path.isfile(os.path.join(r'c:\Users\User\Desktop\automate',filename)):
        print(filename)
        continue
    totalSize = totalSize + os.path.getsize(os.path.join(r'c:\Users\User\Desktop\automate',filename))
print(totalSize)


# delete files and folders

import os 
#permanently delete file
os.unlink('helloworld3.txt')

# delete folder, but can only delete one that is empty
os.rmdir(r'./spare2')

# delete folders, that contain items in it
import shutil
shutil.rmtree(r'spare3')



# to delete files carefully, and with a check first before delete

import os
for filename in os.listdir():
    if filename.endswith('.txt'):
        #os.unlink(filename)
        print(filename)


# send2trash module, delete but send it to recycling bin
# instead of permanently

import send2trash
file
send2trash.send2trash(file)


# reading and writing plaintext file 
# plain text file ( .txt, .py)
# binary file is like a program file ( .exe .doc)

#open file 
helloFile = open('helloworld.txt')
content = helloFile.read()
helloFile.close()
content

# create a new file: open file in write mode, or append mode
helloFile = open('helloworld2.txt', 'w')  # use 'a' for append ( so wont overwrite)
helloFile.write("Yes")




#shelve library, saves list, dictionary., non-text type

import shelve

shelfFile = shelve.open('Mydata')
shelfFile['cats'] = ['Zophie', 'Pooka']




# copying and moving files and folders (32)

# shutil module shell utility, copy and moving files from one folder to another

import shutil

# copy helloworld.txt folder to another folder
shutil.copy(r'helloworld.txt', '.\spare')

# copy the whole folder
shutil.copytree(r'.\spare', '.\spare3')

# move the file and give it another name
shutil.move(r'helloworld.txt', r'helloworld3.txt')



## using os.walk to manipulate files 

# walking a directory tree (34)- IMPT
# using os.walk we can get the folder name, subfolder( one level down) name, and file names
# we can run a look to explore all the folders and files from that directory

import os

# os.walk returns 3 things, it also runs through the whole dictory and loops the fies
for folderName,  subFolders, fileNames in os.walk(r'delicious'):
    print('the folder name: ' + folderName)
    print('the subfolder name: ' + str(subFolders))
    print('the filename: ' + str(fileNames))
    
    # lets say we want to delete subfolders:
    
    for subFolders in subFolders:
        if 'fish' in subFolders:
            os.rmdir(subFolders)
            # just to check if you are deleting the correct file
            #print('rmdir on 'subFolder)
            print()
            
    # duplicate a file and give it a new filename
    for file in fileNames: 
        if file.endswith('.py'):
            shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup'))



# image file sorting template: converting images to greyscale and saving them into a separate directory


import os
from PIL import Image,ImageFilter,ImageOps

where = "images"
outFolder = "grayscale"

def convertImageGrayscale(onlyFirst):
    if not os.path.exists(outFolder):
        os.mkdir(outFolder)
        print("Created grayscale folder successfully.")
    else:
        print("Using current grayscale folder.")
    c = 1
    for root, dirs, files in os.walk(where):
        for file in files:
            fullname = os.path.join(root,file)
            
            if file.lower().endswith("jpg") or \
            file.lower().endswith("bmp") or \
            file.lower().endswith("png") or \
            file.lower().endswith("svg"):

                im = Image.open(fullname)
                out = ImageOps.grayscale(im)
                outFilename = os.path.join(outFolder,file)
                print("get_ipython().run_line_magic("2d", " %s \" % (c, outFilename))")
                out.save(outFilename)
                
                #im.show()
                #display(im)
                #display(out)
                
                c += 1
                if onlyFirst:
                return

convertImageGrayscale(False)
