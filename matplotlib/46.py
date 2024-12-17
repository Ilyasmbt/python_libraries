#BAR WIDTH

#DRAW 4 VERY THIN BARS?
import matplotlib.pyplot as plt
import numpy as np

x=np.array(["a","s","d",'ss'])
y=np.array([1,32,31,19])

plt.bar(x,y,width=0.1)
plt.show()