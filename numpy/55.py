#splitting 2-D arrays

#split the 2-D arrays into three 2-D arrays?

import numpy as ny

arr1=ny.array([[1,2],[3,4],[5,6],[7,8],[9,10],[99,55]])


newarr=ny.array_split(arr1,3)


print(newarr)