# Python Data Analysis - Pandas

# ->Panel data and is the core library for Data Manipulation and Data Analysis
# ->Multi-dimensional structure data set
# ->Pandas is an open-source and under BSD license
# ->Pandas take the data (CSV,Excel,etc.and multiple formats for input)
#   and create python object with rows & columns called data frame

# Uses of Pandas

# 1] Data Creation: You can create tables using Pandas
# 2] Data Loading:  You can load/import table using Pandas
# 3] Extract individual column: You can extract a specific particular column from the table
# 4] Extracting individual records: You can extract specific records from the table based on some condition
# 5] Data Visulisation: You can make Plots using Pandas

# Pandas : High performance Data Analysis
#          Support Files from diff. formats
#          Flexible
#          Work on Missing data
#          Performing indexing,slicing and subsetting large dataset as well as merge & join 2 diff. dataset easily
#          Reshaping Dataset

# DATA STRUCTURES:-
#   1]SERIES (Series working with 2-dimensional using lists,dictionaries and series)
#       --> pd.Series(data, index)
#   2]DATAFRAME (Dataframe working with 3-dimensional) : Most Efficient Data Structure
#       --> pd.Dataframe(data)
#   3]PANEL (Panel working with multi-dimensional, major axis/row and minor axis/column)
#       -->pd.Panel(data, major axis, minor axis, datatype)

import pandas as pd
import numpy as np

l1=[10,20,30,40]
print(pd.Series(l1, index=['i','ii','iii','iv']))
print("\n")

dict1={"Name":["Kush","Maulik","Lekhan"], "Enroll_no":[385,411,389]}

emp=pd.Series()
print("\nEmpty Series: ",emp)

print("\n")
arr=np.array([10,21,32,43])
s1=pd.Series(arr)
print(s1)

dict2={"Name":"Kush","No":385}
print("\n")
print(pd.Series(dict1))
print("\n")
print(pd.Series(dict2,index={"Name":"Karan","No":20}))

tup1=[("a",11),("b",12),("c",13)]
print("\n")
print(pd.Series(tup1))

# Diff. ways to create Dataframe
# 1] Load data from excel,CSV
# 2] Create data frame

df=pd.read_excel("D:\\SampleSheet1.xlsx")
print(df)

print(pd.DataFrame(dict1))
print("\n")

print(pd.DataFrame(l1))
print("\n")

print(pd.DataFrame(tup1))

# SERIES ATTRIBUTES IN PANDAS
#   1] index --> Series.index() : Returns all index values
#   2] array --> Series.array() : Returns all array values
#   3] values --> Series.values() : Returns all values from the series
#   4] name --> Series.name() : Returns name of the series
#   5] shape --> Series.shape() : Returns shape of the the series
#   6] ndim --> Series.ndim() : Returns the dimension of the series
#   7] size --> Series.size() : Returns the size of the series
#   8] nbytes --> Series.nbytes() : Returns memory occupied by the series
#   9] memory_usage --> Series.memory_usage() : Returns memory occupied by both indexing and values from the series
#   10] empty --> Series.empty() : Returns boolean value ( If True --> Empty Series , False --> Non-Empty series)

s=pd.Series(arr,name="ARR_NUMBERS")

print(s.index)
print(s.array)
print(s.values)
print(s.name)
print(s.shape)
print(s.ndim)
print(s.size)
print(s.nbytes)
print(s.memory_usage())
print(s.empty)

arr2=np.array([20,393,93,39])
s2=pd.Series(arr2)

print(s.add(s2))
print(s2.subtract(s))
print(s.multiply(s2))
print(s2.divide(s))
print(s2.mod(s))
print(s2.pow(s))
print(s.le(s2))
print(s.gt(s2))
print(s.equals(s2))

# INDEXING & SLICING DATAFRAME
#   1] head(n) : Returns the first n rows
#   2] tail(n) : Returns the last n rows
#   3] describe() : Basic mathematical formula applied on all columns
#   4] shape() : Returns the no. of rows and columns
#   1] slice(start:stop:step) : Returns sliced data
#   1] iterrows() : Returns the index of rows
#   1] loc(n) : Returns the n rows

print(df.head(3))
print(df.tail(4))
print(df.describe())
print(df.columns)
print(df.shape)

print(df[["Name","Enroll_No"]])

print(df[1:5])
print(df[1::2])
print(df[["Name","Enroll_No"]][1:5])
print(df[["Name","Enroll_No"]].head(5))







