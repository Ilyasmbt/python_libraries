#numerate on following 2-D arrays

import numpy as mp

arr=mp.array([[11,12,13],[14,15,16]])

for idx,x in mp.ndenumerate(arr):
    print(idx,x)