import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

data = load_iris()

X = data.data
y = data.target

pca = PCA(n_components=2)

X_pca = pca.fit_transform(X)

print("PCA Output")
print(X_pca)

plt.scatter(
    X_pca[:,0],
    X_pca[:,1],
    c=y
)

plt.title("PCA")
plt.xlabel("PC1")
plt.ylabel("PC2")

plt.show()