#create a FILTER array that will
#return only odd elements from the original array?

import numpy as np
arr=np.array([41,51,54,56,66])

filter_arr=arr%2==1

newarr= arr[filter_arr]

print(filter_arr)
print(newarr)