import matplotlib.pyplot as plt
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
model = KMeans(
    n_clusters=3,
    random_state=42
)

for i in (dir(plt)):
  if(i.startswith('x')):
    print(i)
