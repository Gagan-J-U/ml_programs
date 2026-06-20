import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# Load Dataset
data = pd.read_csv("ToyotaCorolla.csv")

print(data.head())

# --------------------
# 1. Scatter Plot
# --------------------
plt.figure(figsize=(5,4))
plt.scatter(data["KM"], data["Price"])
plt.title("Scatter Plot")
plt.xlabel("KM")
plt.ylabel("Price")
plt.show()

# --------------------
# 2. Box Plot
# --------------------
plt.figure(figsize=(5,4))
plt.boxplot([data["Price"], data["HP"], data["KM"]])
plt.xticks([1,2,3], ["Price","HP","KM"])
plt.title("Box Plot")
plt.show()

# --------------------
# 3. Heat Map
# --------------------
plt.figure(figsize=(5,4))
corr = data[["Price","KM","HP","Weight"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Heat Map")
plt.show()

# --------------------
# 4. Contour Plot
# --------------------
plt.figure(figsize=(5,4))
plt.tricontourf(data["KM"], data["Weight"], data["Price"], cmap="viridis")
plt.colorbar(label="Price")
plt.xlabel("KM")
plt.ylabel("Weight")
plt.title("Contour Plot")
plt.show()

# --------------------
# 5. 3D Surface Plot
# --------------------
fig = plt.figure(figsize=(6,5))
ax = fig.add_subplot(111, projection='3d')

ax.plot_trisurf(
    data["KM"],
    data["HP"],
    data["Price"],
    cmap="viridis"
)

ax.set_xlabel("KM")
ax.set_ylabel("HP")
ax.set_zlabel("Price")
ax.set_title("3D Surface Plot")

plt.show()