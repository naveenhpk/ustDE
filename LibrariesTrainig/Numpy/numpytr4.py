import numpy as np
a=np.array([
    [4,8],
    [6,1]
])
b=np.array([
    [3,5],
    [7,2]
])
print(np.hstack((a,b))) #combine 2 or more array and aranged horizontally merging
print(np.vstack((a,b))) #combine 2 or more stack and arrange vertically merging
print(np.concatenate((a,b),axis=None)) #concatinating of 2 or more arrays in row/col/flat as in axis