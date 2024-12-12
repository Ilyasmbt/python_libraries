#FORMAT STRING FMT

#YOU can also use the shortcut string notation parameter
#to specify the marker

#this parameter is also called fmt,and is written with this syntax:
#syntax:
#      MARKER|line|COLOR

#MARK EACH POINT WITH A CIRCLE????

import matplotlib.pyplot as plt
import numpy as np

ypoints=np.array([3,8,1,10])

plt.plot(ypoints,'o:r')
plt.show()