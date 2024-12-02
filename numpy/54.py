#access the splitted arrays?

import numpy as ny

arr1=ny.array([1,2,3,4,5,6])


newarr=ny.array_split(arr1,2)

print(newarr[0])
print(newarr[1])