import pandas as pd
iris=pd.read_csv('iris.csv')
print(iris)
# creating ne wcolumn and adding vlaues based on the category
# map is use dto match the value and used to replace then value that is automaticclay maped
iris['setosa']=iris.Species.map({"setosa":1,"versicolor":0,"virginica":0})
print(iris.head())

# creating a dummy
print('*'*50)
specific_dum=pd.get_dummies(iris.Species,prefix="Species").iloc[:,0:]
print(specific_dum)

iris=pd.concat([iris,specific_dum],axis=1)
print(iris.head())
print('*'*50)
# rnaking
print(iris.rank())
# cummualtive sum

iris["cum_sum"]=iris["Sepal.Length"].cumsum()
print(iris.head())
# print(iris.quantile(0.5))
