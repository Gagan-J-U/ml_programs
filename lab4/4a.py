# Best First Search Algorithm

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 5,
    'E': 2,
    'F': 4,
    'G': 0
}

def best_first_search(start, goal):
    open_list = [start]
    visited = []

    while open_list:
        open_list.sort(key=lambda x: heuristic[x])
        node = open_list.pop(0)

        if node not in visited:
            visited.append(node)

            if node == goal:
                return visited

            for neighbor in graph[node]:
                if neighbor not in visited:
                    open_list.append(neighbor)

    return None

path = best_first_search('A', 'G')

print("Path Traversed :", path)