#Labels
#add labels to the pie chart with the labels parameter

#a simple pie chart:

import matplotlib.pyplot as plt
import numpy as np


y=np.array([15,32,25,25])
mylabels=["apple","banana","grapes","dates"]
plt.pie(y,labels=mylabels)
plt.show()