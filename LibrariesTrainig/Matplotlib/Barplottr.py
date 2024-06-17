import matplotlib.pyplot as plt
fig,ax = plt.subplots()
months = ["jan","feb","mar","apr","may","jun","jul"]
temp_rec=[36,42,40,48,38,41,33]
bar_labls=['cool','hot',"mid hot","super hot",'mid-cool',"mid hot","super cool"]
bar_colors=["tab:red","tab:blue","tab:green","tab:blue","tab:brown","tab:green","tab:pink"]
ax.bar(months,temp_rec,label=bar_labls,color=bar_colors)
ax.set_ylabel("Temp by month")
ax.set_title("Monthwise temp records")
ax.legend(title="Temperature by month")
plt.show()