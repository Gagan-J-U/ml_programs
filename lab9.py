import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import dendrogram, linkage

# Load Iris Dataset
data = load_iris()

df = pd.DataFrame(
    data.data,
    columns=data.feature_names
)

# --------------------
# Single Linkage Dendrogram
# --------------------

single = linkage(
    df,
    method='single'
)

plt.figure()
dendrogram(single)

plt.title("Single Linkage Dendrogram")
plt.xlabel("Samples")
plt.ylabel("Distance")
plt.show()

# --------------------
# Complete Linkage Dendrogram
# --------------------

complete = linkage(
    df,
    method='complete'
)

plt.figure()
dendrogram(complete)

plt.title("Complete Linkage Dendrogram")
plt.xlabel("Samples")
plt.ylabel("Distance")
plt.show()