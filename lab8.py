import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

data = load_iris()

df = pd.DataFrame(
    data.data,
    columns=data.feature_names
)

model = KMeans(
    n_clusters=3,
    random_state=42
)

model.fit(df)

labels = model.labels_
centers = model.cluster_centers_

print("Labels:")
print(labels)

print("\nCentroids:")
print(centers)

# Graph
plt.scatter(
    df.iloc[:,0],
    df.iloc[:,1],
    c=labels
)

plt.scatter(
    centers[:,0],
    centers[:,1],
    marker='X',
    s=200
)

plt.title("K-Means Clustering")
plt.xlabel(df.columns[0])
plt.ylabel(df.columns[1])

plt.show()