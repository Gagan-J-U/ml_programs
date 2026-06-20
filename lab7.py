import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("glass.csv")

X = df.drop('Type', axis=1)
y = df['Type']

X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size=0.3,
    random_state=42
)

euclidean = KNeighborsClassifier(
    n_neighbors=3,
    metric='euclidean'
)

euclidean.fit(X_train,y_train)

pred1 = euclidean.predict(X_test)

print("Euclidean Accuracy =",
      accuracy_score(y_test,pred1))

manhattan = KNeighborsClassifier(
    n_neighbors=3,
    metric='manhattan'
)

manhattan.fit(X_train,y_train)

pred2 = manhattan.predict(X_test)

print("Manhattan Accuracy =",
      accuracy_score(y_test,pred2))