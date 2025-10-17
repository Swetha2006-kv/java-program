import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Sample data
data = pd.DataFrame({
    'height': [150, 160, 170, 180, 190, 200],
    'weight': [50, 60, 70, 80, 90, 100],
    'gender': ['M', 'F', 'M', 'F', 'M', 'F']
})

# Create KDE plot
plt.figure(figsize=(5, 4))
sns.kdeplot(data['weight'], shade=True, color='red')  # Corrected data selection and parameters
plt.title("seaborn: KDEplot")
plt.show()
