#multiple points

#you can plot as many points as you like,
#just make sure you have the same number of points in both axis
#draw a line in a diagram from position ?

import matplotlib.pyplot as plt
import numpy as np

xpoints=np.array([1,2,6,8])
ypoints=np.array([3,8,1,10])

plt.plot(xpoints,ypoints)
plt.show()