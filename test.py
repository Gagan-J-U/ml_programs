n=int(input("Enter the number of nodes: "))

for i in range(n):
    print("Enter the node name")
    node=input()
    print("Enter the number of neighbors")
    neighbors=int(input())
    graph[node]=[]
    for j in range(neighbors):
        print("Enter the neighbor name and cost")
        neighbor,cost=input().split()
        graph[node].append((neighbor,int(cost)))