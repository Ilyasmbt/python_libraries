#numpy splitting array

#array_split()---method
#split the array in 3 parts ?

import numpy as ny

arr1=ny.array([1,2,3,4,5,6])

arr=ny.array_split(arr1,3)
newarr=ny.array_split(arr1,4)

print(arr)
print(newarr)