import random

# Objective Function
def objective(x):
    return -(x * x) + 10

# Hill Climbing Function
def hill_climbing(start):
    current = start

    while True:
        left = current - 1
        right = current + 1

        current_value = objective(current)

        # Choose the better neighbor
        if objective(left) > current_value:
            current = left
        elif objective(right) > current_value:
            current = right
        else:
            break

    return current, objective(current)

# Random Starting Point
start = random.randint(-10, 10)

solution, value = hill_climbing(start)

print("Starting Point :", start)
print("Optimal Solution :", solution)
print("Optimal Value :", value)