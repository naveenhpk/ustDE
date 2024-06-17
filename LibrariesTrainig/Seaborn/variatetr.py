import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

card_appr=pd.read_csv('creditcarddataset.csv')
print(card_appr.head())
''' Univariate is the most basic form of dtaa analysis technique.It means we need to aalyse 
the data contained by only one varaible and dont want to deal with cause or effect 

2types: categorical and continues
'''

# univariate  continues data------------------------
# sns.histplot(data=card_appr,x="Age",hue='Gender',kde=True)
# plt.legend(['Male','Female'])
# plt.show()

#univariate for categorical data---------------
# sns.countplot(data=card_appr,hue='Approved',x='Gender')
# plt.legend(['Male','Female'])
# plt.show()

# # how many of bank customers and non bankm customers are applied
# sns.countplot(data=card_appr,hue='Approved',x='BankCustomer')
# plt.legend(['Male','Female'])
# plt.show()

# based on differnt ethinicity
# sns.countplot(data=card_appr,hue='Approved',x='Ethnicity')
# plt.show()



# BIVARIATE ANALYSIS
# the data set contail two variable sand reserchers ain to undertkae comparison bw the 2 data set

# finding correlation b/w diff variables
# print(card_appr[['Age','Debt','YearsEmployed','CreditScore','Income']].corr())
# plt.ylim(0,20000)
# sns.scatterplot(data=card_appr,x='YearsEmployed',y='Income')
# plt.show()

data=card_appr.groupby(by='Approved').mean(['Age','Debt','YearsEmployed','CreditScore','Income'])
print(data)

# sns.kdeplot(data=card_appr,x='Age',hue='Approved',fill=True)
# plt.show()

# sns.kdeplot(data=card_appr,x='CreditScore',hue='Approved',fill=True)
# plt.show()

# multivariate anALYSIS it is used for more complex form of statistical analysis
    # it is used when there are more than two variable in the data set

# sns.pairplot(data=card_appr[['Age','Debt','YearsEmployed','CreditScore','Income','Approved']],hue='Approved')
# plt.show()


