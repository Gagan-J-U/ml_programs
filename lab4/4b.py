# A* Algorithm

graph = {
    'S': [('A', 1), ('G', 10)],
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 5)],
    'C': [('D', 3), ('G', 4)],
    'D': [('G', 2)],
    'G': []
}

h = {
    'S': 5,
    'A': 3,
    'B': 4,
    'C': 2,
    'D': 1,
    'G': 0
}

def a_star(start, goal):
    open_list = [(start, 0)]
    visited = []

    while open_list:
        open_list.sort(key=lambda x: x[1] + h[x[0]])

        node, cost = open_list.pop(0)

        if node == goal:
            return cost

        visited.append(node)

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                open_list.append((neighbor, cost + weight))

    return None

cost = a_star('S', 'G')

print("Minimum Cost :", cost)