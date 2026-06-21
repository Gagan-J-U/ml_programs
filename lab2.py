# Best First Search Algorithm Implementation in Python

from queue import PriorityQueue

graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"Enter node {i+1}: ")
    graph[node] = []

e = int(input("Enter number of edges: "))

print("\nEnter edges in format:")
print("Source Destination Heuristic")

for i in range(e):
    src, dest, h = input().split()
    graph[src].append((dest, int(h)))

start = input("\nEnter start node: ")

pq = PriorityQueue()
pq.put((0, start))

visited = []

print("\nBest First Search Traversal:")

while not pq.empty():

    h, node = pq.get()

    if node not in visited:

        print(node, end=" ")
        visited.append(node)

        for neighbor, cost in graph[node]:
            pq.put((cost, neighbor))