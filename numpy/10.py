#ndmin
#create an array with 5 dimension and verify that it has 5 dimensions?
import numpy as np

arr=np.array([1,2,3,4],ndmin=5)


print(arr)
print('num of dimension :', arr.ndim)