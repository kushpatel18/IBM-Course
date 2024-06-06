# AGGREGATION IN PANDAS
#   It provides various functions that performs a mathematical or logical operation on our dataset and returns a summary
#   of that function.
#   Aggregation can be used to get a summary of columns in our dataset like getting sum,min.,max.,etc. from
#   a particular column of our dataset.
#   The function used is agg(), the parameter is the func. we want to perform.
import pandas as pd
import numpy as np

# Functions:-
#   1] sum(): Summation of column values
#   2] min(): finds min. amongst column values
#   3] max(): finds max. amongst column values
#   4] mean(): Computes mean of column values
#   5] size(): Compute column sizes
#   6] describe(): Generates descriptive statistics
#   7] first(): Compute first of group values
#   8] last(): Computes last of group values
#   9] count(): Compute count of column values
#   10] std(): Std. deviation of column
#   11] var(): Variance of column
#   12] sem(): Computes standard error of column

df=pd.DataFrame({'key':['A','B','C','A','B','C'],'data':range(6)},columns=['key','data'])
print(df)

df_grouped=df.groupby('key').sum()
print("\n",df_grouped)

df_grouped1=df.groupby('key').min()
print("\n",df_grouped1)

df_grouped2=df.groupby('key').max()
print("\n",df_grouped2)

df_grouped3=df.groupby('key').mean()
print("\n",df_grouped3)

df_grouped4=df.groupby('key').size()
print("\n",df_grouped4)

df_grouped5=df.groupby('key').describe()
print("\n",df_grouped5)

df_grouped6=df.groupby('key').first()
print("\n",df_grouped6)

df_grouped7=df.groupby('key').last()
print("\n",df_grouped7)

df_grouped8=df.groupby('key').count()
print("\n",df_grouped8)

df_grouped9=df.groupby('key').std()
print("\n",df_grouped9)

df_grouped10=df.groupby('key').var()
print("\n",df_grouped10)

df_grouped11=df.groupby('key').sem()
print("\n",df_grouped11)

dataset=pd.read_csv("D:\Python\Demo1.csv")
print(dataset.head(3))

print("\n",dataset.describe())

print("\n",dataset.groupby(['Cut','Color']).agg('min'))

print("\n",dataset.agg(['sum','min','max']))

a=dataset.groupby('Maths')
print("\n",a.first())

ipl_data = {'Team':['Riders','Riders','Devils','Devils','Kings','Kings','Kings','Kings','Riders','Royals','Royals','Riders'],
            'Rank': [1,2,2,3,3,4,1,1,2,4,1,2],
            'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
            'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}

df=pd.DataFrame(ipl_data)

grouped=df.groupby('Year')
print("\n",grouped['Points'].agg(np.mean))

grouped2=df.groupby('Team')
print("\n",grouped2.agg(np.size))