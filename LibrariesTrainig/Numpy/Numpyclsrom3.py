# find mean of every numpy array in a given list
import numpy as np
list=[
    np.array([32,6,80,15]),
    np.array([74,2,11,8]),
    np.array([10,51,1,78])
]

# list=np.array([
#     [3,6,8],
#     [7,2,11],
#     [10,5,1]
# ])

result=[]
for i in range(len(list)):
    result.append(np.mean(list[i]))

print(result)