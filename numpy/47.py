#numpy joining array
#joining numpy arrays
#joining means putting contents of two or more arrays in a single array?
#concatenate() function

#join 2 arrays

import numpy as mp

arr1=mp.array([11,12,123])
arr2=mp.array([66,77,88])

arr=mp.concatenate((arr1,arr2))
print(arr)