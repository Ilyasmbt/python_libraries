#numpy Array slicing

import numpy as np

arr=np.array([1,2,3,4,5,6,7])

print(arr[1:4])
#slice elements from index 4 to  the end of the array
print(arr[4:])
#slce elements from the begning to index 4(not included)
print(arr[:4])