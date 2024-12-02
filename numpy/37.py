#flattening the arrays

#flattening array means convertig a multidimensional array into a 10 array

#we can use reshape(-1) to do this.

#convert the array into a 10 array?

import numpy as np

arr= np.array([[1,2,3],[4,5,6]])

newarr= arr.reshape(-1)

print(newarr)