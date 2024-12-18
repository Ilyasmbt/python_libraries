#count plot
#the count plot can be thought of
#as a histogram across a categorical variable

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_context('paper')
#loading dataset
titanic= sns.load_dataset("titanic")

sns.countplot(x="class",hue="who",data=titanic,palette='magma')

plt.title("survivors")
plt.show()