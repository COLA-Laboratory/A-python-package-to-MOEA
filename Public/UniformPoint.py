from itertools import  combinations
import numpy as np

def factorial(n):
    result = 1
    for i in range(2,n+1):
        result*=i
    return result


def comb(n,k):
    return factorial(n)/(factorial(n-k)*factorial(k))

def UniformPoint(N,M):
    H1 = 1;
    while(comb(H1+M, M-1) <= N):
        H1 = H1 + 1

    temp1 = list(combinations(np.arange(H1+M-1), M-1))
    temp1 = np.array(temp1)
    temp2 = np.arange(M-1)
    temp2 = np.tile(temp2, (int(comb(H1+M-1, M-1)), 1))
    W = temp1-temp2
    W = (np.concatenate((W, np.zeros((np.size(W,0),1))+H1), axis=1)-np.concatenate((np.zeros((np.size(W,0),1)), W), axis = 1))/H1

    if H1<M:
        H2 = 0
        while(comb(H1+M-1,M-1)+comb(H2+M,M-1)<=N):
            H2 = H2 + 1
        if H2>0:
            temp1 = list(combinations(np.arange(H2 + M - 1), M - 1))
            temp1 = np.array(temp1)
            temp2 = np.arange(M - 1)
            temp2 = np.tile(temp2, (int(comb(H2 + M - 1, M - 1)), 1))
            W2 = temp1 - temp2
            W2 = (np.concatenate((W2, np.zeros((np.size(W2,0),1))+H2), axis=1)-np.concatenate((np.zeros((np.size(W2,0),1)), W2), axis = 1))/H2
            W = np.concatenate((W,W2/2+1/(2*M)),axis=0)

    realN = np.size(W,0)
    W[W==0] = 10**(-6)
    return W,realN




