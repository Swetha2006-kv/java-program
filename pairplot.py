import seaborn as sns
import matplotlib.pyplot as plt

# Load Iris dataset
iris = sns.load_dataset("iris")

# Create pairplot
sns.pairplot(iris, hue="species", kind="reg")  # Corrected 'category' and 'dig_kind'
plt.suptitle("seaborn: pairplot", y=1.02)
plt.show()
