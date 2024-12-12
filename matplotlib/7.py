#markers

#you can use the keyword arguments marker
#to emphasize each points with a specified marker:

#mark each point with a circle?

import matplotlib.pyplot as plt
import numpy as np

ypoints=np.array([3,8,1,10])

plt.plot(ypoints,marker='*')
plt.show()