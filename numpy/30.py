#view
#make a view,change the org array, and display both arrays?
import numpy as np

arr=np.array([1,2,3,4,5])
x=arr.view()
arr[0]=225

print(arr)
print(x)