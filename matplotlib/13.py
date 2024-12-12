#Matplotlib Line

#use a dotted Line?
#LINESTYLE :
#'solid'  (default)    '-'
#'dotted'    ":'
#'dashed'    '--'
#'dashdot'   '-.'
#'none'  '' or''

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import lineStyles

ypoints=np.array([3,8,1,10])
plt.plot(ypoints,linestyle='dotted')    #linestyle / ls is used
plt.show()