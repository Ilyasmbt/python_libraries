#find the index where the value are even?

import  numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9,10])

x=np.where(arr%2 ==0)
print(x)    #index num

y=np.where(arr%2 ==1)    # for find odd



