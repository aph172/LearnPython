import os
dirName = os.getcwd()
print('Current Directory: ' + dirName)
listOfFiles = os.listdir(dirName)
print (listOfFiles)
fileToOpen = dirName + '\\test.log'
print ('file to open: ' + fileToOpen)

processedData = ''

# Open data file
try:
    rawFile = open(fileToOpen)
    for line in rawFile:
        myContents = rawFile.readline()
        if (myContents.find('UpperAndLowerLimits') >= 0) or (myContents.find('LowerLimitsOnly') >= 0) or (myContents.find('UpperLimitsOnly') >= 0) :
            processedData += myContents
finally:
    rawFile.close()
print(processedData)

#Create a new file with processed data
newfile = dirName + '\\processed.txt'
file_object = open(newfile, 'w')
file_object.write(processedData)
file_object.close()
