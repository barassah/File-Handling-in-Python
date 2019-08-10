#File Handling in python
#creating and Deleting
import os
#checking if file exists before creating 
if os.path.exists('text.txt'):
#	print('File Exist!')
	#inquire overwrite or append content
	#prompt for over witing of file contents
	i=input('Overwrite file? y/n: ')
	if i!=n:
		myfile = open('text.txt', 'a') 
		#appending text to be done
		myfile.write('\nHello there, added Content!')
		myfile.close()
	else:
		myfile = open('text.txt', 'w') 
		#appending text to be done
		myfile.write('Hello there, New Content!')
		myfile.close()
else:
#	print('File Doesn\'t Exist')
	#create a new and opening the file to append new content
	myfile = open('text.txt', 'a') 
	#appending text to be done
	myfile.write('Hello there, New Content!')
	#close file
	myfile.close()
#opening file to read
f=open('text.txt','r')
#read one line using the readdline function
#print(f.readline())
#Read and display the entire content in the text file
for x in f:
	print(x)
#close the file
f.close()
#prompt for deletion of file
d=input('Delete File? y/n: ')
if d!='n':
	# use system defined remove function
	os.remove('text.txt')
	print('File Deleted')
else:
	print('File Not Deleted')
