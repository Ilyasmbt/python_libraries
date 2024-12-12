#set Line PROPERTIES/attributes for the GRID

#set the line properties of the grid?

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

x=np.array([80,85,90,95,100,105,110,115,120,125])
y=np.array([240,250,260,270,280,290,300,310,320,330])

plt.plot(x,y)

plt.title("Sports Day")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.grid(color='yellow',linestyle='--',linewidth=1.5)                      #grid fun using
plt.show()