def alphabeta(depth,node,maxPlayer,
              values,alpha,beta,height):

    if depth == height:
        return values[node]

    if maxPlayer:

        best = -1000

        for i in range(2):

            val = alphabeta(depth+1,node*2+i,False,values,alpha,beta,height)


            best = max(best,val)
            alpha = max(alpha,best)

            if beta <= alpha:
                break

        return best

    else:

        best = 1000

        for i in range(2):

            val = alphabeta(depth+1,node*2+i,True,values,alpha,beta,height)

            best = min(best,val)
            beta = min(beta,best)

            if beta <= alpha:
                break

        return best

values = [3,5,6,9,1,2,0,-1]

result = alphabeta(
    0,0,True,
    values,
    -1000,
    1000,
    3
)

print("Optimal Value =", result)