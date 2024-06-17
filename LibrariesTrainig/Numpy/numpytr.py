import numpy as np
# numpy row and col vector
digits=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(digits)

print(digits.shape)
print("row vector")
row_vector=digits[:,np.newaxis]
print("digits",row_vector)
print('colvector')
col_vector=digits[np.newaxis,:]
print("digits",col_vector)

oddlist=[1,3,5,7,9,11]
ol_numpy=np.array(oddlist)
print(ol_numpy)
print('*'*30)
print("shape of an aray",ol_numpy.shape)
row1_vector=ol_numpy[:,np.newaxis]
print("digits",row1_vector)
print('colvector')
col1_vector=ol_numpy[np.newaxis,:]
print("digits",col1_vector)