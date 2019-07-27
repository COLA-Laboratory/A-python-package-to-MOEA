import numpy as np
import random

def tournamentSelection(Pop,N):
    tournament = 2
    a = round(N/2)
    pop_candidate = np.zeros(tournament)
    pop_rank = np.zeros(tournament)
    pop_cd = np.zeros(tournament)
    pop_parent = []
    for i in range(a):
        for j in range(tournament):
            pop_candidate[j] = round(N*random.random())
            if(pop_candidate[j] == N):
                pop_candidate[j] = N-1
        while (pop_candidate[0] == pop_candidate[1]):
            pop_candidate[0] = round(N*random.random())
            if(pop_candidate[0] == N):
                pop_candidate[0] = N-1
        pop_rank[0] = Pop[int(pop_candidate[0])].paretoRank
        pop_rank[1] = Pop[int(pop_candidate[1])].paretoRank
        pop_cd[0] = Pop[int(pop_candidate[0])].cd
        pop_cd[1] = Pop[int(pop_candidate[1])].cd

        if(pop_rank[0]!=pop_rank[1]):
            index = np.argmin(pop_rank)
            winner = Pop[int(pop_candidate[index])]
            pop_parent.append(winner)
        else:
            index = np.argmax(pop_cd)
            winner = Pop[int(pop_candidate[index])]
            pop_parent.append(winner)
    return pop_parent

def elitism(N,combinePop):
    pop_elitism = []
    index1 = 0
    index2 = 0
    pop_ranked = sorted(combinePop,key = lambda individual:individual.paretoRank)
    flag = pop_ranked[N-1].paretoRank
    for i in range(len(pop_ranked)):
        if(pop_ranked[i].paretoRank == flag):
            index1 = i
            break
        else:
            pop_elitism.append(pop_ranked[i])
    for i in range(len(pop_ranked)):
        if(pop_ranked[i].paretoRank == (flag+1)):
            index2 = i
            break


    tempPop = []
    j = index1
    if(index2 == 0):
        index2 = len(pop_ranked)
    while(j<index2):
        tempPop.append(pop_ranked[j])
        j+=1
    tempPop = sorted(tempPop,key = lambda individual:individual.cd,reverse=True)
    #random.shuffle(tempPop)
    remainN = N-index1

    for i in range(remainN):
        pop_elitism.append(tempPop[i])
    return pop_elitism

def findMaxCurrentIndex(x,chromo_rank):
    max = -1
    for i in range(len(chromo_rank)):
        if(chromo_rank[i].paretoRank==x):
            if(i>max):
                max = i
    return max
def elitism2(N, combine_chromo2,):
    chromo = []
    temp1 = []  # 存放最后一个等级的种群
    preIndex = -1
    currentIndex = -1
    # 根据pareto等级从高到低进行排序
    chromo_rank = sorted(combine_chromo2, key=lambda Individual: Individual.paretoRank)

    max_rank = chromo_rank[N - 1].paretoRank
    # print(max_rank)
    # print(flag)
    for i in range(max_rank):
        currentIndex = findMaxCurrentIndex(i + 1, chromo_rank)
        # print(currentIndex)
        if (currentIndex > (N - 1)):
            remainN = N - preIndex - 1  # 因为index是从0开始的，preindex代表已经算入preindex+1的个数了
            t = preIndex + 1
            while (t <= currentIndex):
                temp1.append(chromo_rank[t])
                t = t + 1
            temp2 = sorted(temp1, key=lambda Individual: Individual.cd, reverse=True)
            for j in range(remainN):
                chromo.append(temp2[j])
            # print (len(chromo))
            return chromo
        elif (currentIndex < (N - 1)):
            t = preIndex + 1;
            while (t <= currentIndex):
                chromo.append(chromo_rank[t])
                t = t + 1
        else:
            t = preIndex + 1;
            while (t <= currentIndex):
                chromo.append(chromo_rank[t])
                t = t + 1
            # print (len(chromo))
            return chromo
        preIndex = currentIndex