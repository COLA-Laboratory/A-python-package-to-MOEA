import numpy as np

def crowdingDistance(F,nonDominatedPop,M):
    #print(len(nonDominatedPop))
    pop_CD = []
    sortedPop = sorted(nonDominatedPop,key = lambda individual:individual.paretoRank)
    currentIndex = 0
    for pareto_rank in range(len(F)-1):
        cd = np.zeros(len(F[pareto_rank+1]))
        tempPop = []
        tempIndex = 0
        tempPopCD = np.zeros((len(F[pareto_rank+1]),M))
        for i in range(len(F[pareto_rank+1])):
            tempPop.append(sortedPop[currentIndex+i])
            tempIndex = i
        currentIndex = currentIndex+tempIndex+1
        #print(len(sortedPop))
        for i in range(M):
            indexObj = [];
            sortedObJ = sorted(tempPop,key = lambda individual:individual.obj[i])
            for j in range(len(sortedObJ)):
                indexObj.append(tempPop.index(sortedObJ[j]))
            #print(len(sortedObJ))
            obj_min = sortedObJ[0].obj[i]
            obj_max = sortedObJ[len(sortedObJ)-1].obj[i]
            tempPopCD[indexObj[0]][i] = float("inf")
            tempPopCD[indexObj[len(indexObj)-1]][i] = float("inf")

            j = 1
            while(j <= (len(indexObj)-2)):
                pre_obj = sortedObJ[j-1].obj[i]
                next_obj = sortedObJ[j+1].obj[i]
                if(obj_max == obj_min):
                    tempPopCD[indexObj[j]][i] = float("inf")
                else:
                    tempPopCD[indexObj[j]][i] = (next_obj-pre_obj)/(obj_max-obj_min)
                j += 1
        cd = np.sum(tempPopCD,axis=1)
        for i in range(len(tempPop)):
            tempPop[i].cd = cd[i]
            pop_CD.append(tempPop[i])
    return pop_CD