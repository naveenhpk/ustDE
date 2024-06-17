import pandas as pd
import numpy as np
df=pd.read_csv("income.csv") #reading the csv file
# Creating data frame
# sample_data=pd.DataFrame({'var1':np.arange(1,20,2)},index=[9,8,7,6,5,4,2,1,3,10])
# print(sample_data)
# # selcting 1st 3 rows
# print(sample_data.iloc[:3])
# print("-"*30)
# # retuns data upto index 3
# print(sample_data.loc[:3])
# print("-"*30)
# # creating data frame
# zodiac_data=pd.DataFrame({"Name":["John","Marry","Julia","Kenny","Henry"],
#                           "Sign":["Libra","Leo","Virigo","Capricon","Aries"]})
# print(zodiac_data)
# print("all columns")
# print(zodiac_data.columns)
# print("-"*30)
# #rename the columns
# zodiac_data.columns=["Names","Zodiac Sign"]
# print(zodiac_data)
# print("-"*30)
# #rename specific Columns
# zodiac_data.rename(columns={"Names":"Customer"},inplace=True) # if inplace is flasse it does not change name but changes inmemmory
# print(zodiac_data)
# print("-"*30)
# print("Replace a particular stiring with in the columns of dataset")
# df.columns=df.columns.str.replace('Y',"Year")
# print(df.columns)
# print("-"*30)
#
#
# print(df.head()) #there is inde with number and char
# print(df.columns)
# df.set_index("Index",inplace=True)
# print(df.head()) #changes index only to char
# print(df.columns)
#
# print("-"*30)
# df.reset_index(inplace=True)
# print(df.head()) #changes index back
# print(df.columns)
#
# print("-"*30)
# #removing col
# df.drop('Index',axis=1,inplace=True) #Index col is removed
# print(df.columns)
# df.drop('State',axis="columns",inplace=True)
# print(df.columns)
#
# print("-"*30)
# # removing rows
# df.drop(0,axis=0,inplace=True)
# print(df.head())
#
# df.drop(1,axis="index",inplace=True)  #removing based on index
# print(df.head())
#
# print("-"*30)
# # removing multiple rows
# df.drop([0,1,2,3,4,5],axis=0,inplace=True)
# print(df.head())

# SOrting
df.sort_values('State',ascending=True,inplace=True)
print(df.head())
# df.Y2002
# df.sort_values()
df.sort_values(["Index","Y2002"],inplace=True)
print(df.tail())