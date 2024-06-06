# Dynamic Typing
# type function is used to identify the datatype of the value assigned to a variable
institute=2
print(institute)
print(type(institute))
institute=["PIET","PIT"]
print(institute)
print(type(institute))

# Assignment Operators
a=10
print(a+10)
a+=10
print(a)
a*=2
print(a)
a/=4
print(a)
a%=2
print(a)
a**=2
print(a)
a//=2
print(a)


print("Name:")
a="Kush"
print(a+" Patel\n")

principal_amount=100
rate_of_interest=2.5
time=2
simple_interest=(principal_amount*rate_of_interest*time)/100
total_balance=principal_amount+simple_interest
print("Simple Interest Amount:",simple_interest)
print("Total Balance:",total_balance)

message='There is a class today'
print(message)
message="There is a class today"
print(message)
print(len(message))
message='"There is a class today"'
print(message)
print(len(message))
# message='There's a class today'
# print(message) ----> Error
message="There's a class today"
print(message)
print(len(message))
message="""\nThere\'s class today
Message was officially shared yesterday
\t\t\t\t\t-By Professor"""
print(message)
print(len(message))

username="Kush Patel_5385"
# String Indexing ---> string_variable[index] index can be +ve or -ve
# Indexing cannot be used to assign different values than the one already declared as strings are immutable
print(username[0])
print(username[13])
print(username[-10])

# String Slicing Format---> string_variable[start:stop:step]
# start represents the index from where the substring sliced begins including the character present at start index
# stop represents the index where the substring sliced ends excluding the Character present at end index
# step represents the the skips taken before selecting a charactrer as a part of sliced string. Default=1
# if no index is given, slicing will assume from beginning of string to ending of string
print(username[5:])
print(username[3:10:2])
print(username[::-1])

# String Concatenation
first_name="Kush"
last_name="Patel"
print(first_name+" "+last_name)     #Both arguments must be strings, otherwise it gives TypeError

# String Replication/Repitition
a="Hello\t"
a*=10
print(a)    #One argument must be int and other argument should be str type

# String methods
string="Hello world"
string2="123"
print(string2.isalnum())
print(string.isalpha())
print(string.istitle())
print(string.upper())
print(string.isupper())
print(string.lower())
print(string.islower())
print(string.split())
print(string.split('o'))
print(string.count('o'))
print(string.capitalize())
print(string.find('w'))
print(string.casefold())
print(string.index('d'))

#Exercise:-
# [1]
print(6*7)
# [2]
print("Number 1\tThe Larch\nNumber 2\tThe Horse Chestnut")