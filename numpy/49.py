#joining arrays using stack function

#stacking is same as concatenation,
#the only difference is that stacking is done along a new axis

#stack()--method

import numpy as ny

arr1=ny.array([1,2,3])
arr2=ny.array([11,12,13])
arr=ny.stack((arr1,arr2),axis=1)
print(arr)