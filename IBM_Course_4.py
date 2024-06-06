# Arithmetic Operators
num1=float(input(("Enter first number:")))
num2=int(input("Enter second number:"))
print("Sum: ",num1+num2)
print("Difference:", num1-num2)
print("Product: ",num1*num2)
print("Division: ",num1/num2)
print("Quotient: ",num1//num2)
print("Remainder: ",num1%num2)
print("Power: ",num1**num2)

# print("Kush"+18) ---> TypeError: can only concatenate str (not "int") to str
print("Kush"+"18")

print(3*"Kush")
print("Kush"*3)
# print(2.5*"Kush")  --->TypeError: can't multiply sequence by non-int of type 'float'
# print("Kush"*"Patel")  ---> TypeError: can't multiply sequence by non-int of type 'str'

# print(num/0) and print(num%0)--->ZeroDivisionError: division by zero

# Relational Operators
a=int(input("Number 1:"))
b=int(input("Number 2:"))
print("a<b: ",a<b)
print("a>b: ",a>b)
print("a<=b: ",a<=b)
print("a>=b: ",a>=b)
print("a==b: ",a==b)
print("a!=b: ",a!=b)

# Read multiple values from keyboard
c,d,e=[int(x) for x in input("Enter three numbers: ").split()] #Must be int values or ypu get
print("Product: ",c*d*e)                                       #ValueError: invalid literal for int() with base 10: '3.5'

f,g,h=[float(x) for x in input("Enter three numbers: ").split()]   #Can accept even int values
print("Product: ",f*g*h)

#Logical Opeartors
# For Boolean information (Compares relational expressions as arguments)
# 1]and --> True only if both arguments are true
# 2]or  --> True if even one of both the arguments is true
# 3]not --> Performs complement of the result of argument

# For Non-Boolean Information
# 0 and empty str means false
# Non-zero means true

str1="Karan"
str2="Kush18"
print(str1 and str2)
print(""and str2)
print(str2 and "")
print(str2 or str1)
print(str2 or "")
print("" or str1)
print(not str1)
print(not "")

h=int(input("Enter any number: "))
print(h>2 and h<10)
print(h>2 or h<10)
print(not h<10)

# Bitwise Opeartors
# Applicable for only int and bool types or we get Error
# 1]& ---> if both bits are 1 , the res. is 1 otherwise 0
# 2]| ---> if at least 1 bit is 1, then res. is 1 otherwise 0
# 3]^ ---> if bits are different,then only res. is 1 otherwise 0
# 4]~ ---> bitwise complement operator [tilde operator]
# 5]<< ---> bitwise left shift
# 6]>> ---> bitwise right shift

# print(1 & 2) and print(True | False) --->Valid
# print(1.5 & 2.5)                     --->Inavalid

print("Bitwise AND: ",0 & True)
print("Bitwise OR: ",0 | True)
print("Bitwise NOT: ",0 ^ True)
print("Bitwise Complement: ",~5)
print("Bitwise Left Shift: ",5<<2)
print("Bitwise Right Shift: ",5>>2)

# eval() Function
# Built-in func. that allows you to evaluate an expression and display the result dynamically
x=10
y=5
result=eval("x**y")
print(result)

