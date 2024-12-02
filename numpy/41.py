

#and in order to enable it in nditer() we pass flags=['buffered']

#iterate through the array as a string:

import numpy as np

arr=np.array([1,2,3])

for x in np.nditer(arr,flags=['buffered'], op_dtypes=['S']):
    print(x)

