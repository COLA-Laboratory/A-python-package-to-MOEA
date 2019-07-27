from Public.checkDominance import checkDominance
import numpy as np

def nonDominatedSort(N,Pop):
    paretoRank = 1
    Sp = {}
    Np = {}
    F = {}
    F[paretoRank] = []
    for i in range(N):
        Sp[i] = []
        Np[i] = 0
        for j in range(N):
            result =checkDominance(Pop[i], Pop[j])
            if(result == 1):
                Sp[i].append(j)
            elif(result == -1):
                Np[i] +=1

        if(Np[i] == 0):
            Pop[i].paretoRank = 1
            F[paretoRank].append(i)
    tempNp = Np.copy()
    #print(len(F[paretoRank]))
    while(len(F[paretoRank])!=0):

        temp = []
        for i in range(len(F[paretoRank])):
            if( len(Sp[F[paretoRank][i]]) != 0 ):
                for j in range(len(Sp[F[paretoRank][i]])):
                    Np[Sp[F[paretoRank][i]][j]] -= 1
                    if( Np[Sp[F[paretoRank][i]][j]] == 0 ):
                        Pop[Sp[F[paretoRank][i]][j]].paretoRank = paretoRank+1
                        temp.append(Sp[F[paretoRank][i]][j])


        paretoRank += 1
        F[paretoRank] = temp
    #print(tempNp)
    #print(F)
    return F, Pop,tempNp