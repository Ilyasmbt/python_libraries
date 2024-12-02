#enumerated iteration using ndenumerate()

#enumeration means mentioning sequence number of something one y one
#sometimes we require corresponding index of the elements while itrating,
# the ndenumerate () method can be used for those usecase.

#enumerate on following 1D arrays elements ?

import  numpy as np

arr =np.array([1,2,3,4,5])

for idx, x in np.ndenumerate(arr):
    print(idx,x)