import numpy as np

def perceptron(x,w,b):

    y = np.dot(x,w) + b

    if y > 0:
        return 1
    else:
        return 0

X = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])

# AND

w = np.array([1,1])
b = -1.5

print("AND Gate")

for i in X:
    print(i, perceptron(i,w,b))

# OR

w = np.array([1,1])
b = -0.5

print("\nOR Gate")

for i in X:
    print(i, perceptron(i,w,b))