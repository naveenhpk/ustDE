import numpy as np
square=np.array([[16,3,2,13],
                 [5,10,11,8],
                 [9,6,7,12],
                 [4,15,14,1]])

for i in range(4):
    sum_row=square[:,i].sum()==34  #check if the sum of row is 34
    sum_col=square[i,:].sum()==34 #check if sum of col is 34
    print(sum_row)
    print(sum_col)

print(square[:2,:2].sum()) #fund sum of 1st 2 elemts and the next 2 elemnt in row ie 16+3 + 2+13
print(square[2:,2:].sum()) #find the sum of 2 elemnts and next 2 elemnt in col ie 16+5 + 9+4

numbers=np.linspace(5,50,24,dtype=int).reshape(4,-1)
print(numbers)

# masking
mask=numbers%5==0
print(mask)
# filtering the numbes from the list
print(numbers[mask])

print("all the values divisible by 5",numbers[mask])
# without assign to a variable
print("all the value divisible by 4",numbers[numbers%4==0])
# Transpose
print(numbers.T)
#sorting
print("Sorted based on col",np.sort(numbers,axis=0))
print("Sorted based on row",np.sort(numbers,axis=1))