#markerfacecolor
#mfc is shorter to set the color inside
#the edge of marker:



#set the FACE COLOR to green?

import matplotlib.pyplot as plt
import numpy as np

ypoints=np.array([3,8,1,10])
plt.plot(ypoints,marker='o',ms=20,mfc='g')    #mfc is used
plt.show()