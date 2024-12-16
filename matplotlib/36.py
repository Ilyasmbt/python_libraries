import matplotlib.pyplot as plt
import numpy as np
x=np.array([10,20,30,40,50])
y=np.array([1,2,3,4,5])
plt.scatter(x,y,color='hotpink')


x=np.array([12,22,32,42,52])
y=np.array([1,2,3,4,5])
plt.scatter(x,y,color='red')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

x=np.array([15,25,35,45,55])
y=np.array([1,2,3,4,5])
plt.scatter(x,y,color='green')


x=np.array([10,20,30,40,50])
y=np.array([21,22,23,24,25])
plt.scatter(x,y,color='yellow')


x=np.array([12,22,32,42,52])
y=np.array([15,25,35,45,55])
plt.scatter(x,y,color='blue')


x=np.array([15,25,35,45,55])
y=np.array([11,21,31,41,51])
plt.scatter(x,y,color='orange')

plt.suptitle('example')
plt.show()