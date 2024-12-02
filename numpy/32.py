#shape of an array

#print the shape of a 2-Darray?

import numpy as np

arr=np.array([[1,2,3,4],[5,6,7,8]])
# 1 2 3 4        it is 1 dimension
# 5 6 7 8       it is 2 dimension

print(arr.shape)
#eg above returns(2,4) ,which means that
#where the first dimension has 2  elements and the second has 4