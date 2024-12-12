#MARKER COLOR

#u can use the keyword arguments markerEdgeColor
#or the shorter mec to set the color of the edge of the marker:

#set the EDGE color to red?

import matplotlib.pyplot as plt
import numpy as np

ypoints=np.array([3,8,1,10])
plt.plot(ypoints,marker='o',ms=20,mec= 'r')      #mec is using markerEdgeColor
plt.show()