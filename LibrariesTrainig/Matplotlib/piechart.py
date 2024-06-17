import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots(figsize=(6,3),subplot_kw=dict(aspect="equal")) #every keyword in dic nave equal aspect
recipe=['375 g flour',
        '75 g sugar',
        '250 g butter',
        '300 g of berries']

data = [float(x.split()[0]) for x in recipe] #[375,75,...
ingredients= [x.split()[-1] for x in recipe]
print(data,ingredients)

# function to convet into percentatge of data used
def func(pct,allvalues):
    absolute=int(np.round(pct/100*np.sum(allvalues))) #375/100 * sum of all value
    return f"{pct:.1f}%\n({absolute:d}g)"  #in chart 7.5% (75g) .1f means number of decimal points  absolute d means without decimal poit if f shows decimal points

# wedgew means slices of chart
wedges,texts,autotexts=ax.pie(data,autopct=lambda pct:func(pct,data),textprops=dict(color="w"))
ax.legend(wedges,ingredients,title="Ingredients",loc="center left",bbox_to_anchor=(1,0,0.8,1))
plt.setp(autotexts,size=8,weight='bold')
ax.set_title=("Bakery a Pie")
plt.show()