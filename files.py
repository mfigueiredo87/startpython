# Python has functions for creating, reading, updating and deleting files.

#Open a file. 'w' is for write
myFile = open('myfile.txt','w')

#Get some info from this file
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love Python, Laravel, NodeJS')
myFile.write(' and Javascript')
myFile.close()

# Append to file
myFile = open('myfile.txt','a')
myFile.write(' I also like MySQL')
myFile.close()

# Read from file
myFile = open('myFile.txt','r+')
text = myFile.read(100)
print(text)
 
