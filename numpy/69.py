#create a filter array that will
#return only even elements from the original array?
import numpy as ny

arr = ny.array([41, 42, 43, 44])

#Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:

   if element %2==0:      #even num
       filter_arr.append(True)
   else:
       filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)