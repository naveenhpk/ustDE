# reverse numpy array
import numpy as np
list=np.array([
    [3,6,8],
    [7,2,11],
    [10,5,1]
])
print(list)
print("reverse array",np.flip(list)) #reverses entirely with change in position
print("reverse array",np.fliplr(list)) #reverse inside the set
print("reverse array",np.flipud(list)) #reverse only the position

