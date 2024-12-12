#create a title for a plot
#you can use the title() function to set a title for the plot

#add a plot title and labels for the x- and y-axis?

import numpy as np
import matplotlib.pyplot as plt

xaxis=np.array([80,85,90,95,100,105,110,115,120,125])
yaxis=np.array([240,250,260,270,280,290,300,310,320,330])

plt.plot(xaxis,yaxis)

plt.title('Sports Watch Data')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show()