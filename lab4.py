#min max

def minimax(depth,node,maxPlayer,values,height):

    if depth == height:
        return values[node]

    if maxPlayer:

        return max(
            minimax(depth+1,node*2,False,values,height),
            minimax(depth+1,node*2+1,False,values,height)
        )

    else:

        return min(
            minimax(depth+1,node*2,True,values,height),
            minimax(depth+1,node*2+1,True,values,height)
        )

values = [3,5,2,9,12,5,23,23]

result = minimax(0,0,True,values,3)

print("Optimal Value =", result)