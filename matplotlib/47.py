#bar Height

#draw 4 very thin bars?

import matplotlib.pyplot as plt
import numpy as np

x=np.array(["a","s","d",'ss'])
y=np.array([1,32,31,19])

plt.barh(x,y,height=0.1)
plt.show()
