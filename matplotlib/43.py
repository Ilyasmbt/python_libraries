#horizontal bars

#barh(0 function

#draw horizontal bars?
import matplotlib.pyplot as plt
import numpy as np

x=np.array(["a","s","d","f"])
y=np.array([1,32,3,10])

plt.barh(x,y)
plt.show()