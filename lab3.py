from queue import PriorityQueue

graph = {
    'A':[('B',1),('C',3)],
    'B':[('D',3),('E',5)],
    'C':[('F',2)],
    'D':[],
    'E':[],
    'F':[]
}

heuristic = {
    'A':6,
    'B':4,
    'C':2,
    'D':1,
    'E':1,
    'F':0
}

pq = PriorityQueue()

pq.put((0,'A'))

cost = {'A':0}
parent = {'A':None}

while not pq.empty():

    f,current = pq.get()

    if current == 'F':

        path = []

        node = current

        while node is not None:
            path.append(node)
            node = parent[node]

        path.reverse()

        print("Goal Reached")
        print("Path =", " -> ".join(path))
        print("Cost =", cost[current])

        break

    for neighbor,weight in graph[current]:

        g = cost[current] + weight

        if neighbor not in cost or g < cost[neighbor]:

            cost[neighbor] = g
            parent[neighbor] = current

            pq.put(
                (
                    g + heuristic[neighbor],
                    neighbor
                )
            )