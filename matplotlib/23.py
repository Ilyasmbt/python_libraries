#position the Titles
#you can use the loc parameter in title(),xlabel,ylabel() to position them
#legal values are:'left',  'right' and 'center'
#'center' is default value

#position the title and ylabel() to the left and top?

import numpy as np
import matplotlib.pyplot as plt

xaxis=np.array([80,85,90,95,100,105,110,115,120,125])
yaxis=np.array([240,250,260,270,280,290,300,310,320,330])

plt.plot(xaxis,yaxis)

plt.title('Sports Watch Data',loc='left')  #loc= right ,left
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage",loc='top')   #loc= top ,center,bottom   //vertical y-axis
plt.show()