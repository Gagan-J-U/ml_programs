from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load Iris Dataset
iris = load_iris()
X = iris.data
y = iris.target

def run_model(test_size):

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )

    model = GaussianNB()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)

    print("\nTrain-Test Split:",
          int((1-test_size)*100), "-",
          int(test_size*100))
    print("Accuracy:", round(acc*100, 2), "%")

# 90-10 Split
run_model(0.1)

# 70-30 Split
run_model(0.3)