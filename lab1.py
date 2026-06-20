import numpy as np
import matplotlib.pyplot as plt

def objective(x):
    return -(x-5)**2 + 25

current = 0

while True:

    neighbour = current + 1

    if objective(neighbour) > objective(current):
        current = neighbour

    else:
        break

print("Optimal Solution =", current)
print("Maximum Value =", objective(current))

# Graph
x = np.arange(0,11,1)
y = [objective(i) for i in x]

plt.plot(x,y)

plt.scatter(
    current,
    objective(current),
    s=100
)

plt.title("Hill Climbing")
plt.xlabel("X")
plt.ylabel("f(x)")

plt.show()