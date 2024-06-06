import Num_Logics_Functions as nlf
def Palindrome(l):
    for i in l:
        j=i[::-1]
        if i==j and len(i)!=1:
            print(i)

def Length(l):
    l.sort(key=len)
    i=-2
    print("\nWords with maximum length: ")
    print(l[-1])
    max=len(l[-1])

    while  len(l[i])==max:
        print(l[i])
        i-=1



def func1():
    s=input("Enter any string: ")
    l1=s.split()
    print("\nPalindrome Strings are: ")
    Palindrome(l1)

# func1()

def func2():
    s=input("\nEnter any string: ")
    l1=s.split()
    Length(l1)

# func2()

def Automorphic(n):

    flag=0
    sqr=n*n
    count=nlf.Count_Digits(n)

    temp=sqr%(10**count)

    if temp==n:
        flag=1

    return flag

def Disarium(n):

    flag=0
    sum=0
    digits=nlf.Digits(n)


    for i in range(1,len(digits)+1):
        sum+=digits[i-1]**i

    if sum==n:
        flag=1

    return flag

def func3():
    n=int(input("Enter a number: "))

    if Automorphic(n)==1:
        print(n,"is an Automorphic number")
    else:
        print(n,"is not an Automorphic number")

def func4():
    n=int(input("Enter a number: "))

    if Disarium(n)==1:
        print(n,"is a Disarium number")
    else:
        print(n,"is not a Disarium number")

# func3()
# func4()

def func5():
    n=int(input("Enter a number: "))
    d1=dict()

    for i in range(n):
        num=int(input())
        if num not in d1.keys():
            d1.setdefault(num,1)
        else:
            d1[num]=1

    print("\nFrequencies of each no.:")
    for key,val in d1.items():
        print(f"{key} : {val}")

# func5()

def func6():
    str1=input("Enter any string: ")
    n=len(str1)

    for i in range(n):
        j=0
        while j<=i:
            print(str1[j],end=" ")
            j+=1
        print()

# func6()

def func7():
    n=int(input("Enter a number: "))

    for i in range(1,n+1):
        print(" "*(n-i),end=" ")
        print("* "*i)

func7()





