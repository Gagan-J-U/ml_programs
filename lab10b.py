import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

data = load_iris()

X = data.data
y = data.target

lda = LinearDiscriminantAnalysis(
    n_components=2
)

X_lda = lda.fit_transform(X,y)

print("LDA Output")
print(X_lda)

plt.scatter(
    X_lda[:,0],
    X_lda[:,1],
    c=y
)

plt.title("LDA")
plt.xlabel("LD1")
plt.ylabel("LD2")

plt.show()