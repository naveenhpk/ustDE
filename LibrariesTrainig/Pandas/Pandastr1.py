# # Pandas is used for data analysis and it iss strong and flexible pytrhon pacakge which hepls with tha data cleaning and wrangling task
#
# advantages :
# 1.creates structured data similar to ms excel spreadsheet
# 2 reads data from varios sources like csv txt xlsx sql databasea
# 3.sleelcts rows and coloumns from data set
# 4.arrange data in acs and desc order
# 5.filtering dataclasses
# 6.summerising data
# 7.Transpose data into wide range and long format
# 8.merging and concatenating  2 dataset

import pandas as pd
df=pd.read_csv("income.csv") #reading the csv file
# print(df)

income_data_col=df.columns #find all colums
print(income_data_col)
print('-'*60)
print("first 2 columns form income dataset",df.columns[0:2])
print('-'*60)
print("Data type for all the columns form income dataset:",df.dtypes)
print('-'*60)
print("Data type of column subject-",df['State'].dtypes)
print('-'*60)
df.Y2008=df.Y2008.astype(float)
print("changing the datat type of Y2008")
print(df.dtypes)
print('-'*60)
print('total number of rows and columns in data  fraME',df.shape)
print('total number of rows in data  fraME',df.shape[0])
print('total number of columns in data  fraME',df.shape[1])
print('-'*60)
print(df.head()) #returns 1st 5 rows and all columns
print('-'*60)
print(df.tail())  #returns last 5 rows and all columns
print('-'*60)
print(df.head(3)) #retturns the first 3 rows similary for tail
print('-'*60)
print(df.iloc[0:5]) #similar for head
print(df[0:5])
print('-'*60)
print("distict value of index")
u_values=df.Index.unique()
print(len(u_values),u_values)
print('-'*60)
u_values_count=df.Index.nunique()
print(u_values_count)

# to find out the bivarate frequency Distribution

print(pd.crosstab(df.Index,df.State))

# creating frequency distribution
# frequency of index in dataset index i sthe column name
fd=df.Index.value_counts(ascending=False)  #depends on the occurence not on the index value
print(fd)
# generatse any random 10 values
print("# generatse any random 10 values",df.sample(n=10))

#retun 5% random valies from the data set
print("5% random valies from the data set",df.sample(frac=0.05)) #rerutn sample of 5%

print("Y2008 Data index with columns INdex and State")
print(df[["Index","State","Y2008"]])  # or df.state df.index ......
# simliartly
print(df.loc[:,["Index","State","Y2008"]])


print("returns rows with index label 0 -2")
print(df.loc[0:2,["Index","State","Y2008"]])

print(":Slecting concecutive columns")
print(df.loc[:,"Index":"Y2005"]) #selecting from a index col to y2008 col rest all skip
print(df.iloc[:,0:3]) # selcting no of columns usinfg index values
