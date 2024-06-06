# Roll No.:24
#Python Developer: Guido Van Rossum
#First Public Appearance/Launch: 20 Feb 1991
#First Introduced: 1989
#Address of Launch: CWI [Netherlands]

name="Kush Patel"
dob= "20/09/2003"
address="Bharuch"
print(f"Details:-\n Name:{name}\n DOB:{dob}\n Address:{address}")

#Python is a general-purpose,dynamic, high-level,interpreted programming language
#Python program is executed 1 line at a time
#Advantages of interpreted language:
# [1] Debugging is easier and portable
# [2] It supports object-oriented programming approach to develop applications
#     Object-Oriented approach helps the programmer to write reusable code and decrease length of code


#Python 2
# [1] Launch:2000
# [2] print is considered as statement
# [3] We have used ASCII code
# [4] The value of a global variable was changing if used in a for loop {Variable Leakage}

#Python 3
# [1] Launch:2008
# [2] print is considered as function
# [3] We have used Unicode
# [4] The value of a global variable is not changeable

#Python applications/uses:
# [1] AI
# [2] ML
# [3] Data Analytics
# [4] Web/Desktop/Mobile Applications
# [5] Games

# SYNTAX OF PYTHON
# Python uses Indentation to identify/define/indicate a block of code
# There is no use of curly braces,semi-colons
# Indentation refers to the spaces at the beginning of code
# It is very important in python however in other programming languages, its just for readability purpose
# Single-Line Comments can be given by Hashtags{#}
# Python does not support multi-line comments however you can use different methods:-
#  1] Consecutive Single_Line Comments
#  2] Using Multi-Line Strings enclosed by triple inverted commas

name="Kush"
en_roll=5385
CGPA=8.7
Sign=True
l1=[1,2.5,1]
t1=(2,"B",5.2)
d1={1:"a",2:"b"}
set1={"a","b",1,2}

print(type(name))
print(type(en_roll))
print(type(CGPA))
print(type(Sign))
print(type(l1))
print(type(t1))
print(type(d1))
print(type(set1))

print(l1.index(1))
print(l1.count(1))
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.append(32)
print(l1)
print(l1.pop())
