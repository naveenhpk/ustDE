import matplotlib.pyplot as plt
weight =[90,70,85,148,168,94,120]
height=[1.2,2.0,3.5,6.7,4.5,2.8,3.8]
fig,ax=plt.subplots() #inside the fig chart ax is the subplot
ax.bar(weight,height)
plt.show()