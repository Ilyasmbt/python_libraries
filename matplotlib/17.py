#LINE WIDTH'
#THE SHORTER lw TO CHANGE THE WIDTH OF THE LINE.

#plot with a 20.5pt wide line?

import matplotlib.pyplot as plt
import numpy as np


ypoints=np.array([3,8,1,10])
plt.plot(ypoints,linewidth='20.5')    #linewidth /lw is used
plt.show()