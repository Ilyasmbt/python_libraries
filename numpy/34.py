#reshape from 1-d to 3-d

#convert the following 1-d array with 12 elements into a 3-D array

#the outermost dimension will have 2 arrays that contains 3 arrays,
#each with 2 elements:


import numpy as np

arr=np.array([1,2,3,4,5,6,10,7,8,9,11,12])

newarr=arr.reshape(2,3,2)   #last 2 idyn ethra element banm ,enn 3 itty 3[] akydh, first 2 index num

print(newarr)