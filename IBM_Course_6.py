# CONTROL STATEMENTS

# # if statement
# name=input("Enter name:")
# if(name=="Kush"):
#     print("Correct User Access")
# print("Login")
#
# # if-else statement
# name=input("Enter name:")
# if(name=="Kush"):
#     print("Correct User Access")
# else:
#     print("Incorrect User Access")
#
#
# num4=int(input("Enter first number:"))
# num5=int(input("Enter second number:"))
#
# if(num4>=num5):
#     print(num4, " is the greatest number")
# else:
#     print(num5, " is the greatest number ")
#
# num1=int(input("Enter first number:"))
# num2=int(input("Enter second number:"))
# num3=int(input("Enter third number:"))
#
# if(num1>=num2):
#     if(num1>=num3):
#         print(num1," is the greatest number")
#     else:
#         print(num3," is the greatest number")
# else:
#     if(num2>=num3):
#         print(num2," is the greatest number")
#     else:
#         print(num3," is the greatest number")

# Exercise 1
# num=int(input("Enter any number:"))
# if(num<1):
#     print(num, "is not present in between 1 to 100")
# elif(num>=1 and num<=100):
#     print(num, "is present in between 1 to 100")
# else:
#     print(num, "is not present in between 1 to 100")

def type_num(num):

    if(num<0):
        print(num," is negative")
    elif(num==0):
        print(num," is zero")
    else:
        print(num," is positive")

# num1=int(input("Enter a number:"))
# type_num(num1)

num2=int(input("Enter a natural number:"))
sum=0
i=1
while(i<=num2):
    sum+=i
    i+=1
print("Sum of first ",n," natural numbers: ",sum)
