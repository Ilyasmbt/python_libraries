#draw two line by specifying
#the x- and y-points value for both lines?

import matplotlib.pyplot as plt
import numpy as np


y1=np.array([3,8,1,10])
x1=np.array([3,8,1,10])
y2=np.array([6,2,7,12])
x2=np.array([6,7,8,9])

plt.plot(x1,y1,x2,y2)

plt.show()