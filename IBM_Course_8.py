#SEQUENCE
#Sequence are contained with items that are accessible by indexing and slicing

    #   SEQUENCE OPERATIONS
    #   1]Concatenation(+)
    #   2]Repitition(*)
    #   3]Membership
    # etc...

    #   TYPES OF SEQUENCE
    #   [1] LIST-[]
    #       Change Value and Store Value - MUTABLE
    #   [2] TUPLE-()
    #       No Change in Value - IMMUTABLE
    #   [3] STRING-" "
    #       Collection of characters
    #   [4] SET-{}
    #       Find unique value
    #   [5] DICTIONARY-{KEY:VALUE}
    #       Key:Value Pair
    #       Ex- dict1 = { name : "kush" } ====> name--> key , "kush"--> value

#LISTS
# List in Python is a built-in structure which stores a collection of different types of objects.
# List are mutable ==> Modification of contents after creation is possible
# Lists are enclosed in [] and objects are separated by comma(,)

colors=["red","black","white","blue"]
print(colors[1])
colors[3]="golden"
print(colors)
colors.append("blue")
print(colors)
colors.remove("golden")
print(colors)

l1=[1,3,5]
l2=[2,4,6]

l3=l1+l2
l4=l1*3
present= 3 in l1

print("List1: ",l1)
print("List2: ",l2)
print("Concatenation: ",l3)
print("Repitition: ",l4)
print(f"Membership: 3 in l1 is {present}")

list1=[ 1 , "Kush", [18,20], (1,2)]
print(list1[3][1])
print(list1)

# LIST FUNCTIONS
#  1] len(list) --> Get the no. of elements
#  2] max(list) --> Find max. value
#  3] min(list) --> Find min. value
#  4] sum(list) --> Count the sum of all elements

# Exercise-1
list_num1=[1,12,18,78,43,7,54]

print("List of integers: ",list_num1)
print("Sum of all numbers: ",sum(list_num1))
print("Maximum Value: ",max(list_num1))
print("Minimum Value: ",min(list_num1))

print("Sorted List in Ascending Order: ",list_num1.sort())
list_num1.append(15)
print("List after addition of new element: ",list_num1)
list_num1.remove(7)
print("List after removal of a specific object: ",list_num1)
is_present=5 in list_num1
print("5 present in list: ",is_present)

# INDEXING IN LISTS
# Indexing is the process of accessing individual elements in a list using their position

# SLICING IN LISTS
# Slicing allows you to extract a portion of list
# Syntax ==> start:stop:step

lt1=[1,2,3,4,5,6,7,8,9]

print("Last Element: ",lt1[-1])
print(lt1[-7])
print(lt1[3:6])
print(lt1[:5])
print(lt1[3:])
print("Even Indexed List: ",lt1[::2])
print("Odd Indexed List: ",lt1[1::2])
print(lt1[1:8:3])
print("Reverse List: ",lt1[::-1])
print(lt1[7:5:-1])
print(lt1[:4:-2])
print(lt1[8::-3])

# LIST METHODS
# 1] append(): Adds element at last of the list
# 2] insert(): Inserts an element at a specific index position
# 3] remove(): Removes the first occurrence of specified element from the list
# 4] pop():
# 5] index():
# 6] count():
# 7] sort():
# 8] reverse():
# 9] extend():
# 10] copy():


