#multiple lines

#plt.plot()functions:

#draw two lines by specifying a plt.plot()
#function for each line:
import matplotlib.pyplot as plt
import numpy as np


y1=np.array([3,8,1,10])
y2=np.array([6,2,7,12])
y3=np.array([10,2,3,5])
plt.plot(y1)
plt.plot(y2)
plt.plot(y3)
plt.show()