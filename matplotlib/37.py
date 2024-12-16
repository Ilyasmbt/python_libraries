#color Each Dot
#note: only c argument
#set your own color of the markers:

import matplotlib.pyplot as plt
import numpy as np
x=np.array([10,20,30,40,50,60])
y=np.array([0,1,2,3,4,5])

colors=np.array(['pink','black','purple','brown','gray','cyan'])
plt.scatter(x,y,c=colors)
plt.show()