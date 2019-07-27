import numpy as np

def FindNeighbour(W,N,M,T):
    B = []
    for i in range(N):
        temp = []
        for j in range(N):
            distance = 0
            for k in range(M):
                distance+=(W[i][k]-W[j][k])**2
            distance = np.sqrt(distance)
            temp.append(distance)
        index = np.argsort(temp)
        B.append(index[:T])
    return B
