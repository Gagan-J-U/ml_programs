import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load Iris Dataset
data = load_iris()

df = pd.DataFrame(
    data.data,
    columns=data.feature_names
)

# --------------------
# Scatter Plot
# --------------------
plt.figure(figsize=(6,4))
plt.scatter(df.iloc[:,0], df.iloc[:,1])
plt.title("Scatter Plot")
plt.show()

# --------------------
# 3D Surface Plot
# --------------------
x = np.arange(len(df))
y = np.arange(len(df.columns))

X, Y = np.meshgrid(x, y)
Z = np.array([df[col] for col in df.columns])

fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z)

plt.title("3D Surface Plot")
plt.show()

# --------------------
# Contour Plot
# --------------------
plt.figure(figsize=(6,4))
plt.contour(df)
plt.title("Contour Plot")
plt.show()

# --------------------
# Heat Map
# --------------------
plt.figure(figsize=(6,4))
sns.heatmap(df)
plt.title("Heat Map")
plt.show()

# --------------------
# Box Plot
# --------------------
plt.figure(figsize=(6,4))
plt.boxplot(df)
plt.title("Box Plot")
plt.show()