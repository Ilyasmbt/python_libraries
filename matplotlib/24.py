#Matplotlib Adding Grid Lines
#ADD grid Lines TO A PLOT
#you can use the grid() function to add grid lines to the plot.



import numpy as np
import matplotlib.pyplot as plt

x=np.array([80,85,90,95,100,105,110,115,120,125])
y=np.array([240,250,260,270,280,290,300,310,320,330])

plt.plot(x,y)

plt.title("Sports Day")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.grid()                      #grid fun using
plt.show()