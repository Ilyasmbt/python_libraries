#shorter syntax
#linestyle can be written as ls.

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import lineStyles

ypoints=np.array([3,8,1,10])
plt.plot(ypoints,ls='--')    #linestyle / ls is used
plt.show()