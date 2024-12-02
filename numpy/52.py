#stacking along height(depth)

#numpy provides a helper a helper function : dstack() to stack along height,
#which is the same as depth.

import numpy as ny

arr1=ny.array([1,2,3])
arr2=ny.array([11,12,13])
arr=ny.dstack((arr1,arr2))
print(arr)