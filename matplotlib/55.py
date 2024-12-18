#legend with header


#add a legend with a header?

import matplotlib.pyplot as plt
import numpy as np


y=np.array([15,32,25,25])
mylabels=["apple","banana","grapes","dates"]
myexplode=[0.2,0,0,0]

plt.pie(y,labels=mylabels,explode=myexplode)
plt.legend(title="FOUR FRUITS")
plt.show()