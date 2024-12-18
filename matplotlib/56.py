

#Matplotlib Histograms

#Histogram

#histogram is a graph showing frequency distributions.

#It is a graph showing the number of observations within each given interval.

#The hist() function will read the array and produce a histogram:

#A simple histogram:

import matplotlib.pyplot as plt

import numpy as np

x = np.random.normal( 170,  10, 250)

#Generating Random Data

#np.random.normal(170, 10, 250)

#generates random numbers from a normal (Gaussian) distribution.

#170 is the mean (average) of the distribution.

#10 is the standard deviation, which measures the spread of the data around the mean.

#250 is the number of random values to generate.

#So, this line creates an array x with 250 values

# that are normally distributed around a mean of 170 with a standard deviation of 10.
plt.hist(x)
plt.show()