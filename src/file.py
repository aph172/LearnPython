import os
dirName = os.getcwd()
print('Current Directory: ' + dirName)
listOfFiles = os.listdir(dirName)
print (listOfFiles)
fileToOpen = dirName + '/src/test.log'
with open(fileToOpen) as file_object:
    myContents = file_object.read()
    print(myContents)