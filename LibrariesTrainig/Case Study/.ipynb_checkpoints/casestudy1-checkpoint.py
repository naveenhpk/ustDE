import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"

#Case study data Collection
#setting column names for the data
columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang','oldpeak', 'slope', 'ca', 'thal', 'target']
data = pd.read_csv(url, names=columns,na_values='?')#navlues means converint ?  to Nan
# print(data)
print("*"*150)

# data cleaning Start----------------------------------------------------
#finding missing value
values_with_nan=data[data.isnull().any(axis=1)]
print(values_with_nan)
# replacing missing values with the mean
data.fillna(data.mean(),inplace=True)
print(data)
print("*"*150)

#Convering male and female valuees to str
# data['sex'].replace(float(1.0),str('male'),inplace=True)
# data['sex'].replace(float(0.0),str('female'),inplace=True)

# converting target values greater than 1 to 1
for i in data['target']:
    if i>1:
        data['target'].replace(i,1, inplace=True)
# print(data.head(30))



# descriptive statistics
print("Descriptive Statistics")
print(data.describe())

# Create a histogram to visualize the distribution of ages in the dataset.Using Matplotlib
# plt.hist(x=data['age'],bins="auto", color='lightgreen', edgecolor="blue")
# plt.xlabel('Age')
# plt.ylabel('Frequency')
# plt.title('Histogram For Age Distribution')
# plt.legend(['age'])
# plt.show()

# Create a bar plot to visualize the distribution of gender in the dataset.Using Seaborn
# data set contain sex 0 and 1 replce them using male and female
# group_sex=data.groupby('sex').size().reset_index(name='count')
# print(group_sex)
# sns.barplot(data=group_sex,x='sex',y='count',palette="Set2",hue='sex')
# plt.xlabel("Gender")
# plt.ylabel('Count')
# plt.title("Gender Distribution")
# plt.legend(group_sex['sex'])
# plt.show()


# Create a count plot to visualize the relationship between chest pain type (cp) and the presence of heart disease (target).
# sns.countplot(data=data,x='cp',hue='target')
# plt.xlabel('Chest pain')
# plt.ylabel('Heart Disease')
# plt.title('Chest Pain Vs Presence of Heart Disease')
# plt.legend(["Heart Disease Present","Heart Disease Not Present"])
# plt.show()

# Create a box plot to visualize the distribution of cholesterol levels (chol) for patients with and without heart disease.
# sns.boxplot(data=data,hue='target',y='chol',palette='Set1')
# plt.ylabel('Cholestrol Level')
# plt.title('Cholesterol level with or without of Heart Disease')
# plt.legend(["Patient","Not Patient"])
# plt.show()

# Create a pair plot to visualize relationships between multiple variables.
# • Use Seaborn to create the pair plot.
# • Include the following variables: age, trestbps, chol, thalach, and target.
# sns.pairplot(data=data,vars=["age","trestbps", "chol", "thalach"],hue='target',diag_kind="kde")
# plt.suptitle('Disease - Target Pair Plot')
# plt.show()

# Create a heatmap to visualize the correlation between different attributes in the dataset.
# • Use Seaborn to create the heatmap.
# • Display the correlation values on the heatmap.

# corr = data.corr()
# sns.heatmap(corr,cmap='Reds', annot=True, fmt='.2f')
# plt.title("correlation")
# plt.show()

