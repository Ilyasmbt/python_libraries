#iterating 3-D arrays

#IN A 3-D ARRAY IT WILL GO THROUGH ALL THE 2-D ARRAYS.

#ITERATE ON THE ELEMENTS OF THE FOLLOWING 3-D ARRAY:

import numpy as np

arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

for x in arr:
    print(x)