from Algorithm.NSGAII.Non_Dominated_Sort import nonDominatedSort
from Public.checkDominance import checkDominance
from Metric.HV import HV

import numpy as np
import time

def Reduce(pop_combine,M):


    F,pop,Np= nonDominatedSort(len(pop_combine),pop_combine)


    v = len(F)
    #print(Np)
    if v > 2:

        temp = [0]*len(pop_combine)
        for i in range(len(pop_combine)):
            temp[i] = Np[i]


            #print(Np[i])
        r = np.argmax(temp)
        #print(r)
        pop = np.delete(pop_combine, r)
        #print(temp)
        #print(r)
    else:
        start1 = time.time()
        #print("here")
        delta = []
        if M == 2:
            index = []
            pop_ranked = sorted(pop_combine, key = lambda individual:individual.obj[0])
            #delta = [float("inf")]*len(pop_ranked)
            for i in range(len(pop_ranked)):
                index.append(pop_combine.index(pop_ranked[i]))

            f1 = []
            f2 = []
            for i in range(len(pop_combine)):
                f1.append(pop_combine[i].obj[0])
                f2.append(pop_combine[i].obj[1])
            f1_max = np.max(f1)
            f2_max = np.max(f2)
            #print(f1_max)
            #print(f2_max)
            refPoint = [f1_max*1.1,f2_max*1.1]

            for i in range(len(pop_ranked)):
                if i == 0:
                    temp = (pop_ranked[i + 1].obj[0] - pop_ranked[i].obj[0]) * (
                            refPoint[1] - pop_ranked[i].obj[1])
                    delta.append(temp)
                elif i == len(pop_ranked)-1:
                    temp = (refPoint[0] - pop_ranked[i].obj[0]) * (
                            pop_ranked[i - 1].obj[1] - pop_ranked[i].obj[1])
                    delta.append(temp)

                else:
                    temp = (pop_ranked[i+1].obj[0] - pop_ranked[i].obj[0]) * (
                                pop_ranked[i - 1].obj[1] - pop_ranked[i].obj[1])
                    delta.append(temp)
            r = np.argmin(delta)
            pop = np.delete(pop_ranked, r)

        else:

            delta = []
            HV_whole = HV(pop_combine)
            for i in range(len(pop_combine)):
                pop_temp = np.delete(pop_combine,i)
                HV_except = HV(pop_temp,flag = 1)
                delta.append(HV_whole-HV_except)
            r = np.argmin(delta)
            pop = np.delete(pop_combine, r)



        #print(len(pop))
    return pop