#scatter Colors
#color/c argument:

#set your own color of the markers?


import matplotlib.pyplot as plt
import numpy as np
x=np.array([10,20,30,40,50])
y=np.array([1,2,3,4,5])
plt.scatter(x,y,color='hotpink')


x=np.array([12,22,32,42,52])
y=np.array([1,2,3,4,5])
plt.scatter(x,y,color='#88c999')

plt.show()