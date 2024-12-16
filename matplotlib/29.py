#draw 2 plot on top of each other?

import matplotlib.pyplot as plt
import numpy as np
x=np.array([10,20,30,40,50])
y=np.array([1,2,3,4,5])
plt.subplot(2,1,1)  #2rows,1 column,1st subplot
plt.plot(x,y)

x=np.array([15,25,35,45,55])
y=np.array([1,2,3,4,5])
plt.subplot(2,1,2)  #2rows,1 column,2nd subplot
plt.plot(x,y)

plt.show()