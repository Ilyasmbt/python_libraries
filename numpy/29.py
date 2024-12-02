#copy
#make a copy, change the org array, and diplay both arrays?

import numpy as np

arr=np.array([1,2,3,4,5])
x=arr.copy()
arr[0]=22

print(arr)
print(x)