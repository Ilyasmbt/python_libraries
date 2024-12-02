#reshaping
#change the shape of array


#the outermost dimension will have 4 arrays, each with 3 elements

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])

newarr=arr.reshape(4,3)  #4column,3rows

print(newarr)

