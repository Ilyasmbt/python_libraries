#STEP 
#USE the step value to determine the step of the slicing:

#return every other elements from index 1 to index 6:

import numpy as np

arr=np.array([1,2,3,4,5,6,7])

print(arr[1:6:2])           #2 is step value position //jumping 2STEP  // SKIPPING 2 STEP

#RETURN EVERY OTHER ELEMENT FROM THE ENTIRE ARRAY
print(arr[::2])