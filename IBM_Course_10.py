# ===============FILE HANDLING==============
# File stores:-
#   1] Very small amount of information
#       Ex- 100 students mobile no.
#   2] Huge amount of information
#       Ex- HDFC Customer Transaction info.
#   3] Very Very Huge amount of information
#       Ex- Youtube Video, Facebook post, Twitter tweets

#   Need of File
#    => To store our data permanently in file

#   Types of Files
#    1] Text File:
#       --> To store character data
#       --> Ex:- abc.txt
#    2] Binary File:
#       --> To store binary data
#       --> Ex:- Videos, Images, Audio File, Zip File, etc.

#   Perform Activities on File

#    1]Open File
#       To open a file:

#       f=open() --------> In-built function
#       f=open(filename,mode)

#      If you want to open the file, then you require two parameters:
#       1] File name (Path)
#       2] Mode (r,w,a,r+,w+,a+,x)

#           i. r = read : Open an existing file for read operation
#                         This is the default mode.

#               f = open('abc.txt','r')
#               FileNotFound ----> Error ( If specified file does not exist )

#           ii. w = write : Open an existing file for write operation
#                           If a file is available and contains some data, then it overwrites
#                           If a file is not available, then python VM creates a file

#               f = open('abc.txt','w')

#           iii. a = append : Open an existing file for append operation
#                             Write and append are similiar, but append does not overwrite the contents of existing file.
#                             It writes to the end of file and prevent data loss

#               f = open('abc.txt','a')
#               If we want to append from a particular operation, we use f.seek()

#           iv. r+ = read and write : First read and if required, then write
#
#               f = open('abc.txt','r+')

#           iv. r+ = read and write : First read and if required, then write
#
#               f = open('abc.txt','r+')

#           v. w+ = write and read : First write and if required, then read
#
#               f = open('abc.txt','w+') ---> Overwrites Existing data

#           vi. a+ = append and read : First append and if required, then read
#
#               f = open('abc.txt','a+')

#           vii. x = Exclusive Mode : To open a file in exclusive mode
#
#               f = open('abc.txt','x')
#               If a file exists, then it gives FileExistingError
#               If a file does not exists, then python VM creates a file

#---------------Binary File------------------

#  Modes: (rb,wb,ab,r+b,w+b,a+b,b)

# After performing any operation, close the file.
#       f.close()

# f=open('abc.txt','w')
# print("Name: ",f.name)
# print("Mode: ",f.mode)
# print("Close: ",f.closed)
# print("Is Readable: ",f.readable())
# print("Is Writable: ",f.writable())
# f.close()
# print("Closed: ",f.closed)

f=open('abc.txt','w')
f.write("\nHello,\n")
list1=["This is\n","Kush Patel\n","This is\n","a simple\n","text file\n","to perform\n"]
f.writelines(list1)
f.write("sample operations\n")
print("\n Data written to file successfully")
f.close()

# Reading character data from file
#   f.read() ---> To read whole data from file
#   f.read(n) ---> To read 'n' characters from file
#   f.readline() ---> To read only one line from file
#   f.readlines() ---> To read all lines from file into a list

print("----------------------------------")
f=open('abc.txt')
first_chars=f.read(6)
print(first_chars)
f.close()

print("----------------------------------")
f=open('abc.txt')
line1=f.readline()
print(line1,end=' ')
line2=f.readline()
print(line2,end=' ')
all_lines=f.readlines()
for line in all_lines:
    print(line,end=' ')
print("----------------------------------")
print(all_lines)
f.close()

print("----------------------------------")
f=open('abc.txt')
all_data=f.read()
print(all_data)
f.close()



