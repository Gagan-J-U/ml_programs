# Artificial Intelligence Lab Programs

## Overview

This repository contains Artificial Intelligence Lab programs implemented in Python. The programs cover data visualization, search algorithms, game-playing algorithms, classification techniques, clustering techniques, dimensionality reduction techniques, and neural networks.

---

# Programs

## 1. Scatter Plot + Hill Climbing Algorithm

### Aim

* Visualize n-dimensional data using Scatter Plot.
* Implement Hill Climbing Algorithm.

### Output

* Scatter Plot visualization.
* Optimal solution and objective value from Hill Climbing.
* Graph of objective function with optimum point.

---

## 2. 3D Surface Plot + Best First Search (BFS)

### Aim

* Visualize n-dimensional data using 3D Surface Plot.
* Implement Best First Search Algorithm.

### Output

* 3D Surface Plot.
* BFS traversal order.

---

## 3. Contour Plot + A* Algorithm

### Aim

* Visualize n-dimensional data using Contour Plot.
* Implement A* Search Algorithm.

### Output

* Contour Plot.
* Goal node search using A*.

---

## 4. Heat Map + Min-Max Algorithm

### Aim

* Visualize n-dimensional data using Heat Map.
* Implement Min-Max Algorithm.

### Output

* Heat Map visualization.
* Optimal Min-Max value.

---

## 5. Box Plot + Alpha-Beta Pruning

### Aim

* Visualize n-dimensional data using Box Plot.
* Implement Alpha-Beta Pruning Algorithm.

### Output

* Box Plot visualization.
* Optimal value after pruning.

---

## 6. Naive Bayes Classifier on Titanic Dataset

### Aim

Develop a Naive Bayes Classifier using the Titanic Dataset.

### Output

* Training Dataset
* Testing Dataset
* Confusion Matrix
* Accuracy Score

### Algorithm Used

* Gaussian Naive Bayes

---

## 7. K-Nearest Neighbors (KNN) on Glass Dataset

### Aim

Develop a KNN Classifier using:

* K = 3
* Euclidean Distance
* Manhattan Distance

### Dataset Split

* 70% Training Data
* 30% Testing Data

### Output

* Training Dataset
* Testing Dataset
* Confusion Matrix
* Accuracy Score

---

## 8. K-Means Clustering on Iris Dataset

### Aim

Perform Unsupervised K-Means Clustering on Iris Dataset.

### Output

* Cluster Labels
* Cluster Centroids
* Cluster Visualization Graph

---

## 9. Agglomerative Clustering

### Aim

Perform Agglomerative Clustering using:

* Single Linkage
* Complete Linkage

### Output

* Cluster Labels
* Single Linkage Graph
* Complete Linkage Graph

---

## 10. Principal Component Analysis (PCA) and Linear Discriminant Analysis (LDA)

### Aim

Implement PCA and LDA for dimensionality reduction.

### Output

#### PCA

* Reduced Dataset
* PCA Scatter Plot

#### LDA

* Reduced Dataset
* LDA Scatter Plot

---

## 11. Single Layer Perceptron

### Aim

Develop a Single Layer Perceptron to implement:

* AND Gate
* OR Gate

### Output

* Truth Table for AND Gate
* Truth Table for OR Gate

---

# Datasets Used

| Program                  | Dataset         |
| ------------------------ | --------------- |
| Visualization Programs   | Iris Dataset    |
| Naive Bayes              | Titanic Dataset |
| KNN                      | Glass Dataset   |
| K-Means                  | Iris Dataset    |
| Agglomerative Clustering | Iris Dataset    |
| PCA                      | Iris Dataset    |
| LDA                      | Iris Dataset    |

---

# Required Libraries

Install the required libraries:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

---

# Common Imports

```python
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from queue import PriorityQueue

from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

from sklearn.naive_bayes import GaussianNB

from sklearn.neighbors import KNeighborsClassifier

from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering

from sklearn.decomposition import PCA

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
```

---

# Frequently Used Functions

## Train-Test Split

```python
train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)
```

## Accuracy Score

```python
accuracy_score(
    y_test,
    y_pred
)
```

## Confusion Matrix

```python
confusion_matrix(
    y_test,
    y_pred
)
```

## K-Means

```python
KMeans(
    n_clusters=3,
    random_state=42
)
```

## Agglomerative Clustering

```python
AgglomerativeClustering(
    n_clusters=3,
    linkage='single'
)
```

## PCA

```python
PCA(
    n_components=2
)
```

## LDA

```python
LinearDiscriminantAnalysis(
    n_components=2
)
```
