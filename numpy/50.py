#stacking along rows

#numpy provdes a helper function:hstack() to stack along rows.

import numpy as ny

arr1=ny.array([1,2,3])
arr2=ny.array([11,12,13])
arr=ny.hstack((arr1,arr2))
print(arr)