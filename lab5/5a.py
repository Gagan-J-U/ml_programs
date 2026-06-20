# Min-Max Algorithm

values = [3, 5, 2, 9, 12, 5, 23, 23]

def minimax(depth, index, isMax):
    if depth == 3:
        return values[index]

    if isMax:
        return max(
            minimax(depth + 1, index * 2, False),
            minimax(depth + 1, index * 2 + 1, False)
        )
    else:
        return min(
            minimax(depth + 1, index * 2, True),
            minimax(depth + 1, index * 2 + 1, True)
        )

result = minimax(0, 0, True)

print("Optimal Value :", result)
