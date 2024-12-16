#draw 2 plots on the same fig?


import matplotlib.pyplot as plt
import numpy as np
#day one ,the age and speed of 5 cars ?
x=np.array([50,40,30,20,10])
y=np.array([1,2,3,4,5])
plt.scatter(x,y)

#day two ,the age and speed of 10 cars ?
x=np.array([50,40,30,20,10,60,70,80,90,100])
y=np.array([6,7,8,9,10,1,2,3,4,5])
plt.scatter(x,y)


plt.show()

