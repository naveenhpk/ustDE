import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('PatientInfo.csv')
print(df.head())

# drop the age with valule missing
df=df.dropna(subset=['age'])
total_pat_age=df['age'].value_counts().rename_axis('age').reset_index(name="patient_count") #if rename and reset not given noheader
print(total_pat_age)
plt.figure(figsize=(10,10))
plt.pie(total_pat_age.patient_count,labels=total_pat_age.age,startangle=90,autopct='%.if%%')
plt.title("'Age of patients")
plt.show()