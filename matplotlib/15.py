#line color
#arguments color or
#the shorter c to set the color of the line;


#set the line color to red?

import matplotlib.pyplot as plt
import numpy as np


ypoints=np.array([3,8,1,10])
plt.plot(ypoints,color='r')    #color /c is used
plt.show()