#startangle

import matplotlib.pyplot as plt
import numpy as np


y=np.array([15,32,25,25])
mylabels=["apple","banana","grapes","dates"]
plt.pie(y,labels=mylabels,startangle=45)
plt.show()
