import pandas as pd
data='C:/Users/Kush Patel/Downloads/archive/investments.csv'

df=pd.read_csv(data)
# print(df.head(10))
# print("\n",df.tail(10))

# perm=[[i,j,k] for i in range(2) for j in range(2) for k in range(3)]
# print(perm)


# n=int(input())
# arr=[]
# i=0
#
# while i<n:
#     name=input()
#     score=input()
#     arr.append([name, score])
#     i+=1
#
# def Sec_Low(arr):
#
#     min=arr[0][1]
#     for i in arr:
#         if i[1]<min:
#             min=i[1]
#
#     temp=[]
#     for i in arr:
#         if i[1]!=min:
#             temp.append(i)
#     # print(temp)
#
#     sec_min=temp[0][1]
#     for i in temp:
#         if i[1]<sec_min:
#             sec_min=i[1]
#
#     names=[]
#     for i in temp:
#         if i[1]==sec_min:
#             names.append(i[0])
#
#     names.sort()
#     c=len(names)
#
#     if c>=1:
#         for i in names:
#             print(i)
#     else:
#         return
#
# if n>=2 and n<=5:
#     Sec_Low(arr)

n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

def Average(stud,name):

    marks=[]
    for i in stud:
        if i==name:
            marks=stud[name]

    # print(marks)
    total=float()
    for j in range(len(marks)):
        total+=marks[j]

    # print(total)
    avg=float(total/len(marks))
    print(avg)


Average(student_marks,query_name)

