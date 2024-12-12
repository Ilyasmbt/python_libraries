#marker size(MS)

#YOU CAN use the keyword arguments markersize
#or the shorter version,ms to set the size of the number
#set the size of the marker to 20?

import matplotlib.pyplot as plt
import numpy as np

ypoints=np.array([3,8,1,10])
plt.plot(ypoints,marker='o',ms=20)     #ms is used MARKERSIZE
plt.show()