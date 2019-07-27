import numpy as np



def TournmentSelection(utility,N,M):
    winnerIndex = []
    tournament = 10
    a = round(N/5)-M
    pop_candidate = np.zeros(tournament)
    pop_utility = np.zeros(tournament)

    for i in range(a):
        flag = np.zeros(N)
        for j in range(tournament):
            temp = np.floor(N*np.random.rand())
            while flag[int(temp)] == 1:
                temp = np.floor(N*np.random.rand())
            pop_candidate[j] = temp
            flag[int(pop_candidate[j])] = 1
            pop_utility[j] = utility[int(pop_candidate[j])]

        index = np.argmax(pop_utility)

        winnerIndex.append(pop_candidate[index])

    return winnerIndex

def MOEADDRAselection(utility,W, N, M):
    searchIndex = []
    temp = (np.sum(W<0.001,1) == M-1)
    for i in range(len(temp)):
        if(temp[i]):
            #print("here")
            searchIndex.append(i)


    winnerIndex = TournmentSelection(utility, N, M)
    #print("here1!")
    for i in range(len(winnerIndex)):
        searchIndex.append(winnerIndex[i])

    return searchIndex