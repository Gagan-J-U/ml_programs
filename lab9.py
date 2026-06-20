import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering

data = load_iris()

df = pd.DataFrame(
    data.data,
    columns=data.feature_names
)

# Single Linkage
single = AgglomerativeClustering(
    n_clusters=3,
    linkage='single'
)

single_labels = single.fit_predict(df)

print("Single Linkage")
print(single_labels)

plt.scatter(
    df.iloc[:,0],
    df.iloc[:,1],
    c=single_labels
)

plt.title("Agglomerative - Single Linkage")
plt.show()

# Complete Linkage
complete = AgglomerativeClustering(
    n_clusters=3,
    linkage='complete'
)

complete_labels = complete.fit_predict(df)

print("\nComplete Linkage")
print(complete_labels)

plt.scatter(
    df.iloc[:,0],
    df.iloc[:,1],
    c=complete_labels
)

plt.title("Agglomerative - Complete Linkage")
plt.show()