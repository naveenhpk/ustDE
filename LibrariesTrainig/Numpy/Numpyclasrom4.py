# How to add rows and cols in numpy array
import numpy as np
list=np.array([
    [3,6,8],
    [7,2,11],
    [10,5,1]
])
row=[2,4,5]
col=[[2],[4],[5]]
print("add row",np.vstack([list,row]))
print("add col",np.hstack([list,col]))