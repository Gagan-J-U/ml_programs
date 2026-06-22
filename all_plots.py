import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("ToyotaCorolla.csv")

print(df.head())

# --------------------
# Scatter Plot
# --------------------
plt.scatter(df["Price"], df["KM"])
plt.title("Price vs KM")
plt.xlabel("Price")
plt.ylabel("KM")
plt.show()

# --------------------
# Simple 3D Plot
# --------------------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_trisurf(
    df["Age"],
    df["KM"],
    df["Price"]
)

ax.set_xlabel("Age")
ax.set_ylabel("KM")
ax.set_zlabel("Price")

plt.title("3D Plot")
plt.show()

# --------------------
# Contour Plot
# --------------------
plt.tricontour(df["KM"],df["Weight"],df["Price"])

plt.title("Contour Plot")
plt.show()

# --------------------
# Heat Map
# --------------------
sns.heatmap(
    df[["Price", "Age", "KM", "HP", "Weight"]]
        .corr(),
    annot=True
)

plt.title("Heat Map")
plt.show()

# --------------------
# Box Plot
# --------------------
plt.boxplot(
    [
        df["Price"],
        df["KM"],
        df["HP"],
        df["Weight"]
    ]
)

plt.xticks(
    [1, 2, 3, 4],
    ["Price", "KM", "HP", "Weight"]
)

plt.title("Box Plot")
plt.show()