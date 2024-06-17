# print checck board pattern for nxn matix
import numpy as np
n=8
matrix=np.zeros((n,n),dtype=int)
matrix[::2,1::2]=1 #select 0,2,4,6
matrix[1::2,::2]=1 #select 1,3,5,7
print(matrix)
