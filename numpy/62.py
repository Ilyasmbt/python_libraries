#search from the Right side


#find the indexes where the value 7 should be inserted,
#starting from the right side?

import numpy as np

arr= np.array([6,7,8,9])

x=np.searchsorted(arr,7,side='right')
print(x)