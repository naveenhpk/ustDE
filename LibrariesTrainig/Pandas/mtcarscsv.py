import pandas as pd
# read csv file
print("read csv file")
mtcars=pd.read_csv("mtcars.csv")
print(mtcars)
print("*"*100)

print('total number of rows and columns in data ',mtcars.shape)
print('total number of rows in data ',mtcars.shape[0])
print('total number of columns in data',mtcars.shape[1])

print("distict value of cyl")
u_values=mtcars.cyl.unique()
print(len(u_values),u_values)
print('-'*60)


#Extrsct Column names
print("Extrsct Column names")
col_names=mtcars.columns
print(col_names)
print("*"*100)

# selecting 1st 5 rows
print("selecting 1st 5 rows")
print(mtcars.head())
print("*"*100)
print(mtcars.iloc[:5])
print("*"*100)

# selcting the last 5 rows
print("selcting the last 5 rows")
print(mtcars.tail())
print("*"*100)

# select first 2 columns
print("select first 2 columns")
print(mtcars.iloc[:,:2])
print("*"*100)

# selct column by name
print("selct column by name")
print(mtcars[["mpg","drat"]])
print("*"*100)
print(mtcars.loc[:,["mpg","drat"]])
print("*"*100)

# select random number of rows
print("select random number of rows")
print(mtcars.sample(n=20))
print("*"*100)

# selecting fraciton of random values
print("selecting fraciton of random values")
print(mtcars.sample(frac=0.9))
print("*"*100)

# rename th variable
print("rename th variable")
# mtcars.rename(columns={"mpg":"MPG"},inplace=True)
# print(mtcars.head())
print("*"*100)

# selecting a column as index
print("selecting a column as index")
print(mtcars.set_index('mpg'))
print("*"*100)

# finding the bivertate ftrequency distribution
print("bivertate ftrequency distribution")
print(pd.crosstab(mtcars.mpg,mtcars.cyl))
print("*"*100)

print("frequency distribution")
print(mtcars.cyl.value_counts(ascending=False))
print("*"*100)

# removing rows and columns
print("removing columns")
# mtcars.drop("mpg",axis=1,inplace=True)
# mtcars.drop("cyl",axis="columns",inplace=True)
# print(mtcars.head())
print("*"*100)

print("removing rows")
# mtcars.drop(0,axis=0,inplace=True)
# print(mtcars.head())
print("*"*100)

print("removing based on index")
# mtcars.drop(1,axis="index",inplace=True)  #removing based on index
# print(mtcars.head())
print("*"*100)


# # removing multiple rows
print("removing multiple rows")
# mtcars.drop([0,2,3,4,5],axis=0,inplace=True)
# print(mtcars.head())
print("*"*100)

# sorting the variables
print("sorting the variables")
# mtcars.sort_values('mpg',ascending=True,inplace=True)
# print(mtcars.head())
print("*"*100)

print("sorting the variables by 2 col")
# mtcars.sort_values(['disp','hp'],inplace=True)
print(mtcars.head(15))
print("*"*100)


# grouping the variables
print("grouping the variables")
print(mtcars.groupby(['gear','carb']).agg({"disp":['min','max'],'wt':'mean'}))
print("*"*100)
print("grouping and finding the median of that category")
print(mtcars.groupby('gear')["qsec"].median())
#
# finding mean of a col
print("mean of a column qsec")
qsec_mean=mtcars.qsec.mean()
print(qsec_mean)
print("*"*100)

#finding the min value of a col
print("min value of a col qsec")
print(mtcars.qsec.min())
print("*"*100)

#finding the max value of 2
print("finding the max value of 2 col")
print(mtcars.loc[:,["qsec","drat"]].max())
print("*"*100)

# finding the difference
print("finding the difference")
# mtcars['Difference wt-qsec']=mtcars.wt-mtcars.qsec
# mtcars['Difference wt-drat']=mtcars.eval("wt-drat")
# print(mtcars.head())
print("*"*100)


# assigning a calculation to a col
print("finding a calculated value of w col disp and drat in ratio col")
data=mtcars.assign(ratio=(mtcars.disp/mtcars.drat))
print(data.head())

#numerical colums only calculation of std min max etc
print(mtcars.describe())
print("*"*100)

# filtering
print("filtering data using gear")
print(mtcars[mtcars.gear==4])
print("using iloc")
print(mtcars.loc[mtcars.gear==4,:])
print("selcting gear having carb")
print(mtcars.loc[mtcars.carb==4,:].gear)
print("*"*100)


# selction based
# filter the cars with gear 3 and hp>100
print("filter the cars with gear 3 and hp>100")
print(mtcars.loc[(mtcars.gear==3) & (mtcars.hp>100)])
print("*"*100)
print("filter the cars with gear 3 or 4 suing is in")
print(mtcars.loc[mtcars.gear.isin([3,4])])
print("*"*100)
print("Using query hp>100 & gear==3")
print(mtcars.query('hp>100 & gear==3'))
print("*"*100)


# creating dummy
print("Dummy")
mt_dummy=pd.get_dummies(mtcars.mpg,prefix="mpg").iloc[:,0:]
print(mt_dummy)
print("*"*100)

# concating
print("concatnating dummy and mtcard")
concat=pd.concat([mtcars,mt_dummy],axis=1)
print(concat)
print("*"*100)

# cummulative sum
print("cummulative sum")
mtcars["cum_sum"]=mtcars["disp"].cumsum()
print(mtcars.head())
print("*"*100)

#Ranking
print("Ranking")
print(mtcars.rank())

#Quantile
print("Quantile")
print(mtcars.quantile(0.5))