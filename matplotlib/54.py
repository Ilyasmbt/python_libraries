#LEgend
#add a legend?

import matplotlib.pyplot as plt
import numpy as np


y=np.array([15,32,25,25])
mylabels=["apple","banana","grapes","dates"]
myexplode=[0.2,0,0,0]

plt.pie(y,labels=mylabels,explode=myexplode)
plt.legend()                           #legend  to add a list
plt.show()