string="Hello world"
string2="133"
string3="Kush18"
string4="Maulik"
string5="1"
print(string2.find('3'))
print(string.split('l'))
print(string.split())
print(string.index('d'))
print(string.lower())
print(string.islower())
print(string.upper())
print(string.isupper())
print(string.capitalize())
print(string3.isalnum())
print(string2.isalnum())
print(string2.isdigit())
print(string2.isnumeric())
print(string4.isalpha())
print(string4.isalnum())
print(string2.count('3'))
print(string2.endswith('3'))
print(string3.startswith('K'))
print(string.swapcase())
print(string.casefold())
print(string.index('r'))
print(string4.istitle())
print(string.isidentifier())
print(string.isprintable())
print(string.isspace())
print(string2.join(string5))
print(string2.replace("1","3"))

string6="""Hello Parul University
Welcome to Parul University
Welcome to 
\t\tParul University\n\n
How are you?"""
print(string6)

word1="Hello"
word2="Kush"
word3="Welcome"
word4="to"
word5="Parul University "
print(f"{word1} {word2}\n{word3} {word4} {word5}")

print(word5*5)

# Writing To The Screeen
# [1] open():Return a file object and is most commonly used with 2 arguments:- file name and access mode
#     Ex: open(File_name,"r")
#           r->read
#           a->append (Any data written to the file is automatically added to the end)
#           w->write
#           r+ -> read & write

# There are 3 ways to write a value:-
# Expression,Print,Write

# Expression Statements(mostly interactive) are used to compute & write value or to call procedure
# a function that returns no meaningful result
# Procedure in Python return the value None
