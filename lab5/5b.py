# Alpha-Beta Pruning Algorithm

values = [3, 5, 2, 9, 12, 5, 23, 23]

def alphabeta(depth, index, isMax, alpha, beta):

    if depth == 3:
        return values[index]

    if isMax:
        best = float('-inf')

        for i in range(2):
            value = alphabeta(depth + 1,
                              index * 2 + i,
                              False,
                              alpha,
                              beta)

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        for i in range(2):
            value = alphabeta(depth + 1,
                              index * 2 + i,
                              True,
                              alpha,
                              beta)

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best

result = alphabeta(
    0, 0, True,
    float('-inf'),
    float('inf')
)

print("Optimal Value :", result)