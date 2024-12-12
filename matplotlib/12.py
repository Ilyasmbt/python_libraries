#use both the mec and mfc
#arguments to color the entire marker;

#set the color

import matplotlib.pyplot as plt
import numpy as np

ypoints=np.array([3,8,1,10])
plt.plot(ypoints,marker='o',ms=20,mfc='g',mec='y')    #mfc is used
plt.show()