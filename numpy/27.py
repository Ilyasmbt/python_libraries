#change data type from integer to boolean?
import numpy as np

arr=np.array([1,0,3,4])
newarr=arr.astype(bool)
print(newarr)
print(newarr.dtype)