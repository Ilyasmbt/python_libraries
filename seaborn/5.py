import seaborn as sns
import matplotlib.pyplot as plt
#loading dataset
data= sns.load_dataset("iris")
#draw plot
sns.barplot(x="species",y="sepal_length",data=data)

plt.title("title")
plt.show()