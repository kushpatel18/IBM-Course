# # ASSIGNMENT OPERATORS:
# # Compound Operators is combination of arithmetic/binary operators with assignment operator(=)
# # The assignment operators are:-
# #   1]  +=
# #   2]  -=
# #   3]  *=
# #   4]  /=
# #   5]  //=
# #   6]  %=
# #   7]  **=
# #   8]  &=
# #   9]  |=
# #   10] ^=
# #   11] <<=
# #   12] >>=
# x=10
# x&=5
# print(x)  # ---> because Bitwise And on 1010 and 0101 results in 0000
#
# #TERNARY/CONDITIONAL OPERATORS:
# # x = firstValue if condition else secondValue
# # If condition is True, then firstValue is considered otherwise secondValue will be considered
#
# a=int(input("Enter First Number: "))
# b=int(input("Enter Second Number: "))
# min=a if a<b else b
# print("Minimum Value:",min)
#
# # SPECIAL OPERATORS:
# # Python defines 2 special operators:-
#
# # 1] IDENTITY OPERATORS:
# #     There are 2 identity operators available generally used for address comparision:-
# #       [1] is ---> Returns true if both operands are pointing the same object
# #       [2] is not ---> Returns True if both operands are not pointing the same object
# l1=[1,2,3]
# l2=[1,2,3]
# print(id(l1))
# print(id(l2))
# print(l1 is l2)
# print(l1 is not l2)
# print(l1 == l2)
#
# # 2] MEMBERSHIP OPERATORS:
# #     There are 2 membership operators which are used to check whether given object is present in given collection:-
# #       [1] in ---> Returns True if obj. is present in specified collection
# #       [2] not in ---> Returns True if obj. is not present in specified collection
# str="Hello! This is Kush Patel here "
# print('R' in str)
# print('!' in str)
# print('K' not in str)
# print('Kush' in str)
# #OPERATOR PRECEDENCE
# # If multiple operators are present, then which operator will be evaluated first is decided by operator precedence
# print(3/2*4+3+(10/5)**3-2)
#
# #MODULES
# import math as m
# print(dir(m))
# print(m.ceil(5.4))
# print(m.floor(5.8))
# print(m.factorial(7))
# print(m.exp(2))
# print(m.isqrt(5))
# print(m.isnan(i))
#
# # from math import  pi
# rad=float(input("Enter radius of circle: "))
# print("Area of Circle: ",m.pi*rad**2)


# PROJECT 1: WORD ANALYSER INCLUDING COUNTING NO. OF CHAR(S), CHECKING IF WORD IS PALINDROME
#           AND IDENTIFYING THE NO. OF VOWELS AND CONSONANTS IN WORD

string = input("Enter any String: ")
string2=string[::-1]

if(string.lower()==string2.lower()):
    print(string, " is palindrome")
else:
    print(string," is not palindrome")

char=len(string)
print("No. of characters:",char)
vowels=0
consonants=0



for i in string:
    if(i =='a' or i=='e' or i=='i' or i=='o' or i=='u' ):
        vowels+=1
    elif(i==" "):
        continue
    else:
        consonants+=1

print("No. of vowels:",vowels)
print("No. of consonants:", consonants)