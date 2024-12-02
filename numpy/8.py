#3-D arrays
# an array that has 2-D arrays(matrix) as its element is called 3-Darraays
#THESE ARE often used to represent a 3rd order tensor



#CREATE A 3-D ARRAYWITH TWO 2-D ARRAYS,
#both containing two arrays with the value1,2,3 and 4,5,6?
import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr)