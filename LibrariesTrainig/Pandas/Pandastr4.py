import pandas as pd
import numpy as np
df=pd.read_csv("income.csv") #reading the csv file

# Filtering

print(df[df.Index=="A"])
print(df.loc[df.Index=="A",:])

# multiple filtering
print(df.loc[df.Index=="A",:].State) #Select ststes having index a
print("*"*69)
#To filter te rows with index as "A" and income data for 2002>1500000
data=df.loc[(df.Index=="A") & (df.Y2002>150000)]
print(data)


print("*"*69)
# To filter the row with index as "A " and income for data 2002=150000
print("To filter the row with index as 'A' and income for data 2002=150000")
data1=df.loc[(df.Index=="A") & (df.Y2002==1500000)]
print(data1)

# To filter the rows with index either A or W
data2=df.loc[(df.Index=="A") | (df.Index=="W") ]
print(data2)

print(df.loc[df.Index.isin(["A","W"]),:])


print(df.query('Y2002>1700000 &Y2003>1500000'))
