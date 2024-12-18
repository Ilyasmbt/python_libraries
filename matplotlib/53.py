#COLORS

#you can set the color of each wedge with the colors parameter.

#specify a new color for each wedge:

import matplotlib.pyplot as plt
import numpy as np


y=np.array([15,32,25,25])
mylabels=["apple","banana","grapes","dates"]
mycolours=["black","hotpink","b","#4CAF50"]

plt.pie(y,labels=mylabels,colors=mycolours)
plt.show()