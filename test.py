import numpy as np
from queue import PriorityQueue

graph={}

pq=PriorityQueue()
pq.put((0,start))
visited=[]
while not pq.empty():
    v,c=pq.get()
    if c not in visited:
        visited.append(c)
        for c,n in graph[cur]:
            pq.put((c,n))

