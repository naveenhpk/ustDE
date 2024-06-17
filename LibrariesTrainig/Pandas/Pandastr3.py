import pandas as pd
import numpy as np
df=pd.read_csv("income.csv") #reading the csv file
# df["differernce"]=df.Y2008-df.Y2009
# print("Calculate diff")
# print(df.head())
# df["differernce"]=df.eval("Y2008-Y2009")
# print("Calculate diff using eval")
# print(df.head())
#
# #assignning value as a ratrio for assignning data should be ccollected to variable
# print("*"*50)
# data=df.assign(ratio=(df.Y2002/df.Y2003))
# print(data.head())
# print("*"*50)
# print(df.describe()) #numerical colums only calculation of std min max etc
# print("*"*50)
# print(df.describe(include=["object"])) #for strings and object only

print("*"*50)
# print(df.mean)
# print(df.median)
# print(df.agg(["mean","median"]))
#
print("*"*50)
y2008_mean=df.Y2008.mean()
print(y2008_mean)
print(df.Y2008.min())
print(df.loc[:,["Y2002","Y2008"]].max)

print("*"*50)
# group by
# print(df.groupby("Index")["Y2002","Y2003"].min())
print(df.groupby("Index").agg({"Y2002":["min","max"],"Y2003":"mean"}))

# renaming
print("*"*50)
datatranf=df.groupby("Index").agg({"Y2002":["min","max"],"Y2003":"mean"})
datatranf.columns=["Min-2002","Max-2002","Y2003-mean"]
print(datatranf)

print("*"*50)
print(df.groupby(["Index","State"]).agg({"Y2002":["min","max"],"Y2003":"mean"}))


