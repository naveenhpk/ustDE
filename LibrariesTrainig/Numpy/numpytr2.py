import numpy as np

grades=np.array([72,35,64,88,51,90,74,12])
CURVE_CENTER = 80  #SETING 80 AS MID POINT
def curve(grades):
    average=grades.mean() #created mean of each grade
    print(average)
    change=CURVE_CENTER-average #create a new curve
    new_grades=change+grades #
    return np.clip(new_grades,grades,100)

print("original Grades",grades)
print("curve_grades",curve(grades))


# Vectorization
# broadcasting
print("batting average")
# shaping an array to 2 array of 2X3 matrix
# reshape(6,2) reshapr array to 6 row of 2 col
batting_average=np.array([53.3,35.5,88.39,38.0,49.9,38.6,31.3,77.6,34.5,19.6,20.8,66.6]).reshape(2,2,3)
print("Original",batting_average)
print("Swapped",np.swapaxes(batting_average,1,2))

batting_average1=np.array([53.3,35.5,88.39,38.0,49.9,38.6,31.3,77.6,34.5,19.6,20.8,66.6]).reshape(3,4)
print("Batting average",batting_average1)
# axis wise finding maximun and inimum
print("Maximum batting average for each colum",batting_average1.max(axis=0))
print("Minimum batting average for each row",batting_average1.min(axis=1))

dummyarray0=np.zeros((10,2)) #CREARIND AARRAY OF ZEROS OF 10 REOWS AND 2 COL
print("dummy array of zeros",dummyarray0)
dummyarray1=np.ones(10,dtype=int)#setting array as integer arry
print("dummy array of ones",dummyarray1)

dyanamicarry1=np.arange(10,100,5,dtype=int).reshape(3,3,2)# zero to 100 with 5 jumpedd
print(dyanamicarry1)
dyanamicarry2=np.arange(10,100,5,dtype=int).reshape(3,6)# zero to 100 with 5 jumpedd
print(dyanamicarry2)
dyanamicarry3=np.arange(10,100,5,dtype=int).reshape(3,6)# zero to 100 with 5 jumpedd
print(dyanamicarry3)

sumofaray=dyanamicarry2+dyanamicarry3
print("sum of array",sumofaray)

mulofaray=dyanamicarry2*dyanamicarry3
print("mul of array",mulofaray)


