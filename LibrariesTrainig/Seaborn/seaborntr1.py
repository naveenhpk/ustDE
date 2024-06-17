# seaborn is powerful python datavisualiztion tool library that is built on the top of matplotlib
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import seaborn as sns
# import numpy as numpy
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# print(sns.get_dataset_names())
tips=sns.load_dataset('tips')
print(tips.head())
gap=px.data.gapminder()
print(gap)
""""
sns.relplot(data=tips,x="total_bill",y="tip",kind="scatter")
plt.title("Total Bill vs Tip")
plt.show()"""

# g=sns.scatterplot(data=tips,x="total_bill",y="tip")
# g.set_title("Total Bill vs Tip")
# plt.show()

# india=gap[(gap["country"]=="India")]
# sns.relplot(data=india,y="lifeExp",x='year',kind="line")
# plt.title("YoY life Expatancy of india")

# sns.displot(data=tips)
# plt.show()

# g=sns.barplot(data=tips,x='day',y='total_bill',estimator=np.median,errorbar=None) #try withoutnerror bar
# g.set_title('Day wise Total Bill')
# plt.show()
#
# g=sns.pointplot(data=tips,x='day',y='tip',hue='sex')
# g.set_title("day wise tip")
# plt.show()


sns.catplot(kind="box",data=tips,y='tip')
plt.title('Distribution of tips')
plt.show()