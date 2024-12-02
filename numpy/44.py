#iterate arrays using nditer()

#iterate through the following 3-D array

import numpy as mp

arr=mp.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

for x in mp.nditer(arr):
    print(x)