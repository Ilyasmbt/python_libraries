#loading dataset-scatterplot

import seaborn as sns
import matplotlib.pyplot as plt
#loading dataset
data= sns.load_dataset("iris")
#draw plot
sns.scatterplot(x="sepal_length",y="sepal_width",data=data)

plt.title("title")
plt.show()