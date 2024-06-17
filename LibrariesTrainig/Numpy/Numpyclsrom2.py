# sort the given element using numpy
import numpy as np
array=np.array([
    [3,6,8],
    [7,2,11],
    [10,5,1]
])

print("Soting the whole array",np.sort(array,axis=None))
print("Soting the  array row wise",np.sort(array,axis=1))
print("Soting the array col wise",np.sort(array,axis=0))