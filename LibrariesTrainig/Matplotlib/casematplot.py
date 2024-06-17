import pandas as pd
import matplotlib.pyplot as plt

casefile=pd.read_csv('Case.csv')
#selecting province
# province=casefile.loc[:,'province']
# # print(province)
# confirmed=casefile.loc[:,'confirmed']
group=casefile.groupby('province')['confirmed'].sum().reset_index()
print(group)
fig,chart=plt.subplots(layout='constrained')
chart.bar(group.province,group.confirmed)
plt.xticks(rotation=85)
plt.xlabel("Province")
chart.set_ylabel("Accumulated num confirmed")
chart.set_title("No of corona cases in south korea")
plt.show()