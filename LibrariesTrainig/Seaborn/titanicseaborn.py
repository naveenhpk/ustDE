import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# Use Seaborn to create a visualization of
# the Titanic dataset. The visualization should show the relationship between the
# passenger's age and survival.
#
#


# (Scatterplot)
titanic=sns.load_dataset('titanic')
print(titanic)
# pallete changes colour hue sepate using bvalues
# sns.scatterplot(x='age',y='survived',data=titanic,palette="Set1",hue='sex')
# plt.show()

# using a different type of plot, such as a line plot or a bar chart.
# lineplot
# sns.lineplot(x='age',y='survived',data=titanic,palette="Set3",hue='sex')
# plt.show()

# barplot
# sns.barplot(x='age',y='survived',data=titanic,palette="Set3",hue='sex',width=1.5)
# plt.xticks(rotation=-90)
# plt.show()

# adding additional variables to the plot, such as the passenger's class or gender.
# using different colors or shapes to represent the different values of the variables.
# sns.lineplot(x='age',y='survived',data=titanic,palette="Set3",hue='pclass')
# plt.show()


#
# adding a legend to the plot.
line=sns.lineplot(x='age',y='survived',data=titanic,palette="Set1",hue='sex')
plt.legend(labels=['Male','Female'])
fig=line.get_figure()
plt.show()

# saving the plot
fig.savefig("titanic.pdf",format='pdf')