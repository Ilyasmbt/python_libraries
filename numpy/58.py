#use the hsplit() method tosplit the 2-D array

#into three 2-D arrays along rows?
#vsplit()--- along columns
#dsplit(0-- depth (height)


import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])

nwarr=np.hsplit(arr,3)
print(nwarr)