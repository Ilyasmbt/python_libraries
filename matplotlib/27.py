#MATPLOTLIB subplot
#DISPLAY multiple plots
#with the SUBPLOT() FUNCTION

#draw 2 plots?

import numpy as np
import matplotlib.pyplot as plt

#PLOT 1:

x=np.array([80,85,90,95,100,105,110,115,120,125])
y=np.array([240,250,260,270,280,290,300,310,320,330])

plt.subplot(1,2,1)    #(1 row,2 columns,1st subplot)
#subplot thayal kodthalw title elu a plot kodkan kyullu

plt.title("Sports Day")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.grid(color='yellow',linestyle='--',linewidth=1.5)    #grid fun using
plt.plot(x,y)

#plot 2:

x=np.array([80,85,90,95,100,105,110,115,120,125])
y=np.array([240,250,260,270,280,290,300,310,320,330])

plt.subplot(1,2,2) #(1 row,2 columns ,2nd subplot)
plt.plot(x,y)

plt.show()


