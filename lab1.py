# Hill Climbing Algorithm Implementation in Python

import numpy as np
import matplotlib.pyplot as plt

def objective(x):
    return -(x-5)**2 + 25

current = 0

while True:

    left = current - 1
    right = current + 1

    best = current

    if objective(left) > objective(best):
        best = left

    if objective(right) > objective(best):
        best = right

    if best == current:
        break

    current = best

print("Optimal Solution =", current)
print("Maximum Value =", objective(current))

# Graph
x = np.arange(0,10,0.1)
y = [objective(i) for i in x]

plt.plot(x,y)
plt.scatter(x,y, color='black',s=1 )
plt.scatter(
    current,
    objective(current),
    marker='x',
    color='red',
    s=100
)

plt.title("Hill Climbing")
plt.xlabel("X")
plt.ylabel("f(x)")

plt.show()