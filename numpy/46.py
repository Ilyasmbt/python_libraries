#join two 2-D arrays along rows(axis=1)

import numpy as mp

arr1=mp.array([[1,2],[3,4]])
arr2=mp.array([[5,6],[7,8]])

arr=mp.concatenate((arr1,arr2),axis=1)
print(arr)


#axis=1 ---- column wise
#axis=0 ---- row wise