import pandas as pd
import numpy as np
mydata={'Crop':['Rice','Wheat','Barley','Maize'],
        'Yield':[1010,1025.2,1404,1251.7],
        'Cost':[102,np.nan,20,68]}

df=pd.DataFrame(mydata)
print(df)
print("Null cost crop")
print(df.isnull())
print("Not null cost crops")
print(df.notnull())
print("No of crops with no cost")
print(df.isnull().sum())
print("drop the row with missing values")
print(df.dropna(how="any").shape) #drop th entire row even when if 1 column value is missing

print(df.dropna(how="all").shape) #drop th entire row even when if all column value is missing

# print(df.dropna(how="any",subset=['Yield','Cost']).shape) #drop th entire row if either yeild or cost data is missing
# print(df.dropna(how="all",subset=['Yield','Cost']).shape) #drop th entire row if either yeild and cost data is missing
# df["Cost"].fillna(value="unknown", inplace=True)
# x=df.method({"Cost": "Unknown"}, inplace=True)
print(df)
print(df.loc[df.duplicated(),:])
print(df.loc[df.duplicated(keep="first"),:])


