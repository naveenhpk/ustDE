import matplotlib.pyplot as plt
import numpy as np
species=["Adelie","Chinstrap","Gentoo"]
penguin_means={
    "Bill Depth":(18.35,18.43,14.98),
    "Bill Length":(38.79,48.83,47.50),
    "Flipper length":(189.95,195.82,231.19)
}

x=np.arange(len(species))
width=0.25 #width of the bar
multiplier=0

fig,ax=plt.subplots(layout='constrained') #fit inside subplot clearly
for attr,measure in penguin_means.items():
    offset =width*multiplier
    rects=ax.bar(x+offset,measure,width,label=attr)
    ax.bar_label(rects,padding=3)
    multiplier+=1

ax.set_ylabel("length (mm)")
ax.set_title("penguin Attribute by species")
ax.set_xticks(x+width,species)
ax.legend(loc='upper left',ncols=3)
ax.set_ylim(0,250)
plt.show()