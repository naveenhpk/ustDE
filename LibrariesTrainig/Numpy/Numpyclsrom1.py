# search maximum and minimum number using given array
import numpy as np
array = np.arange(20).reshape(5,-1)
print(array)
print("Maximum element in col",np.max(array,axis=0))
print("Maximum element indices in col",np.argmax(array,axis=0))
print("Maximum element in rows",np.max(array,axis=1))
print("Maximum element indices in rows",np.argmax(array,axis=1))