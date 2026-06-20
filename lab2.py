from queue import PriorityQueue

graph = {
    'A':[('B',4),('C',2)],
    'B':[('D',5),('E',7)],
    'C':[('F',1)],
    'D':[],
    'E':[],
    'F':[]
}

pq = PriorityQueue()
pq.put((0,'A'))

visited = []

while not pq.empty():

    h,node = pq.get()

    if node not in visited:

        print(node,end=" ")
        visited.append(node)

        for neighbor,cost in graph[node]:
            pq.put((cost,neighbor))