import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# for linear data
# total_matches_played=[100,50,60,35,45,19,100]
# avg_score=[4000,3500,6000,3500,4500,1000,1500]
# avg_score_ipl=[4500,3090,6100,3600,2500,1700,3580]
# plt.plot(total_matches_played,avg_score,label="Icc Tounamments",linestyle='dotted')
# plt.plot(total_matches_played,avg_score_ipl,label="IPL Tounamments",color="green",marker="*")
# plt.title("Matches Played Vs Average Scores")
# plt.xlabel("Total num of matches PLayed")
# plt.ylabel("Average Score")
# plt.legend()
# plt.show()


x=[1,2,3,4,5]
y=[3,7,4,18,25]
y1=[2,10,11,12,14]
y2=[6,8,18,21,15]
y3=[9,10,14,17,22]
fig,plotting=plt.subplots(nrows=2,ncols=2,figsize=(10,6))
plotting[0,0].plot(x,y,color='yellow',label="Line 1")
plotting[0,0].set_title('Plot1')
plotting[0,1].plot(x,y1,color='green',label="Line 2")
plotting[0,1].set_title('Plot2')
plotting[1,0].plot(y1,y2,color='red',label="Line 3")
plotting[1,0].set_title('Plot3')
plotting[1,1].plot(x,y3,color='purple',label="Line 4")
plotting[1,1].set_title('Plot4')
plt.tight_layout()
plt.show()