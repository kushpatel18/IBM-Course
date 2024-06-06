#   TUPLE: Same as List, but Immutable(Disallows Add,Remove,Replace operation)
#   Read-only version of list

t1=(1,2,3,"Kush")
print(type(t1))
print(t1[0])
print(t1[-1])
print(t1[1:3])
# t1[0]=10          ---> Type Error
# t1.append(20)     ---> Attribute Error
# t1.remove(3)      ---> Attribute Error

# k1=()               --->Tuple type
# k2=(10)             --->Int type
# k3=(10,)            --->Tuple type
# print(type(k))

#Dictionary is not a sequential data structure

#LIST:
#   1] Mutable
#   2] Uses []
#   3] More memory to store elements
#   4] Less Performance
#   5] Slower access to elements
#   6] Review or Comment Section (Facebook,Youtube,Twitter)

#TUPLE:
#   1] Immutable
#   2] Uses ()
#   3] Less memory to store elements
#   4] More Performance
#   5] Faster access to elements
#   6] Bank Account Type(Saving/Current)

#   DICTIONARY: Used to store data values in key:value pairs separated with coma(,) and enclosed in curly braces {}
#               Dictionary is a collection which is ordered,changeable and do not allow key duplication

#       KEYS: Immutable data types, cannot be changed once assigned
#       VALUES: Can have any data type,even duplicate values are allowed but are updated


d1={1:"Kush",1:"Karan",3:"Aayush",4:"Marmik"}
print(type(d1))
print(d1)
print(d1[1])
print(d1.values())
print(d1.keys())

#       DICTIONARY FUNCTIONS

#   1] len(): Returns length/no. of items of dictionary
print(len(d1))

#   Creating Dictionary using dict() Constructor
#   => dict() constructor can take different forms of input to create dictionaries

# 1] Empty dict.
d2=dict()
print(d2)

# 2] From key:value pairs
d3=dict([(1,"kush"),(2,"karan")])
print(d3)

# 3] Using keyword arguments
d4= dict(name="Kush",age=20)
print(d4)

# 4] Copying Dictionary

original_dict={1:"Kush",2:20}
new_dict=dict(original_dict)
print(new_dict)

# 5] Using Dictionary Comprehension[ dict={expression,iteration,condition} ]

numbers=[1,2,3,4,5]
squared_dict={num:num**2 for num in numbers}
print(squared_dict)

#   Accessing Items in Dictionary

# 1] Using [key]
d5={"name":"karan","age":20}
name=d5["name"]
print(name)

# 2] Using get(key) method : Allows you to access a value by specifying the key as an argument
age=d5.get("age")
country=d5.get("country","India")
print(age)
print(country)

# 3] Using items() method: Returns a view object that provides key-value pairs
d6= dict(name="Kush",age=20)
print(d6.items())

# for item in d6.items():
#     print(f"Key:{d5.keys()}")

# 4] Using variable as a key: Use a variable to access a value in a dictionary

og_dict={1:"Kush",2:20}
age=2
print(og_dict[age])

# 5] Using a Loop

for key in d5.keys():
    print(f"Key:{key} Value:{d5[key]}")

#   Changing Value in Dictionary
#   =>Change the values associated with specific keys by simply assigning a new value to that key

print(d6)
d6["age"]=21
print(d6)

#   Update Dictionary

#    1] Using update() method: Allows you to add or update multiple key:value pairs from another dictionary

d6.update(d1)
print(d6)

#   2] Using Dictionary Comprehension

my_dict={"name":"Kush","age":20,"city":"Bharuch"}
updated_dict={key:value + 1 if key=="age" else value  for key, value in my_dict.items()}
print(updated_dict)

#   Removing Items

#    1] Using del Statement: del Statement to remove a specifc item by specifying the key

del my_dict["name"]
print(my_dict)

#    2] Using pop() method: Allows you to remove an item by specifying the and it returns the value associated with that key.
                            #                           It is useful when you want to remove an item and retrieve its value.

my_dict={"name":"Kush","age":20,"city":"Bharuch"}
removed_name=my_dict.pop("name")
print(removed_name)
print(my_dict)

#   3] Using popitem() method: It removes and returns an arbitrary key-value pair as a tuple.
#                               It is useful when you want to remove items without specifying a particular key.

my_dict={"name":"Kush","age":20,"city":"Bharuch"}
removed_item=my_dict.popitem()
print(removed_item)
print(my_dict)

#   4] Using clear() method: Remove all items from a dictionary using the clear() method.

my_dict={"name":"Kush","age":20,"city":"Bharuch"}
my_dict.clear()
print(my_dict)

#   Loop Through a Dictionary

#    1] Loop Through Keys: for loop to iterate through the keys of a dictionary
my_dict={"name":"Kush","age":20,"city":"Bharuch"}

for key in my_dict:
    print(key)

#    2] Loop Through Values: for loop to iterate through the values of a dictionary
my_dict={"name":"Kush","age":20,"city":"Bharuch"}

for value in my_dict:
    print(value)

#    3] Loop Through Key-Value Pairs: for loop to iterate through the items of a dictionary
my_dict={"name":"Kush","age":20,"city":"Bharuch"}

# for key,value in my_dict:
#     print(f"{key}:{value}")

#   Copy Dictionary

#    1] Using copy() method {Shallow Copy}
my_dict={"name":"Kush","age":20,"city":"Bharuch"}
copied_dict=my_dict.copy()
print(copied_dict)

#    2] Using dict() constructor
my_dict={"name":"Kush","age":20,"city":"Bharuch"}
copied_dict=dict(my_dict)
print(copied_dict)

#    3] Using the copy Module {Deep Copy}: To create a deep copy of dictionary, where both keys and values
#                                          are copied recursively, you can use copy module's deepcopy() function.

import copy

my_dict={"name":"Kush","age":20,"city":"Bharuch"}
copied_dict=copy.deepcopy(my_dict)
print(copied_dict)

#   Nested Dictionaries: A dictionary can contain dictionaries

family={"child1":{"name":"Kush","age":21},"child2":{"name":"Aashka","age":15}}
print(family)
print(family["child2"]["name"])

#   DICTIONARY METHODS

#   1] clear()
#   2] copy()
#   3] get(key,default)
#   4] items()
#   5] keys()
#   6] values()
#   7] pop(key,default)
#   8] popitem()
#   9] update(dictionary)
#  10] setdefault(key,default): Returns the value for a key if it exists, otherwise sets a default value for the key
#                               and returns it

d5={"name":"karan","age":20}
age=d5.setdefault("age",21)
city=d5.setdefault("city","Bharuch")
print(age)
print(city)
print(d5)



