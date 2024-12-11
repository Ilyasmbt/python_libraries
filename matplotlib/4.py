#plotting without Line

#to plot only the  markers,
#you can use shortcut string notation parameter 'o',
#which means 'ring'.

#draw a line in a diagram from position(1,8) to position (3,10)?

import matplotlib.pyplot as plt
import numpy as np

xpoints=np.array([1,8])
ypoints=np.array([3,10])

plt.plot(xpoints,ypoints,'o')
plt.show()