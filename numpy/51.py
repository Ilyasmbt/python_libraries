#stacking along columns

#numpy provides a helper function:vstack() to stack along columns.

import numpy as ny

arr1=ny.array([1,2,3])
arr2=ny.array([11,12,13])
arr=ny.vstack((arr1,arr2))
print(arr)