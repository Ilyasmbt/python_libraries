#draw 6 plot?

import matplotlib.pyplot as plt
import numpy as np
x=np.array([10,20,30,40,50])
y=np.array([1,2,3,4,5])
plt.subplot(2,3,1)  #2rows,1 column,1st subplot
plt.plot(x,y)

x=np.array([15,25,35,45,55])
y=np.array([1,2,3,4,5])
plt.subplot(2,3,2)  #2rows,1 column,2nd subplot
plt.plot(x,y)

x=np.array([10,20,30,40,50])
y=np.array([1,2,3,4,5])
plt.subplot(2,3,3)  #2rows,1 column,3 subplot
plt.plot(x,y)

x=np.array([15,25,35,45,55])
y=np.array([1,2,3,4,5])
plt.subplot(2,3,4)  #2rows,1 column,4 subplot
plt.plot(x,y)

x=np.array([10,20,30,40,50])
y=np.array([1,2,3,4,5])
plt.subplot(2,3,5)  #2rows,1 column,5 subplot
plt.plot(x,y)

x=np.array([15,25,35,45,55])
y=np.array([1,2,3,4,5])
plt.subplot(2,3,6)  #2rows,1 column,6 subplot
plt.plot(x,y)

plt.show()