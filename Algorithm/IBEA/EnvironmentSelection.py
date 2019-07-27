import numpy as np


def EnviromentSelection(pop_mixed,fitness,N):
    pop_new = []
    flag = np.ones(len(pop_mixed))

    for i in range(N):
        for j in range(len(pop_mixed)):
            if(flag[j] == 1 ):
                worst = j
                break


        for j in range(len(pop_mixed)):
            if(flag[j]!=0):
                if(pop_mixed[j].fitness > pop_mixed[worst].fitness):
                    worst = j

        flag[worst] = 0

        for j in range(len(pop_mixed)):
            if(flag[j]==1):
                pop_mixed[j].fitness -= fitness[worst][j]

    for i in range(len(pop_mixed)):
        if(flag[i] == 1):
            pop_new.append(pop_mixed[i])

    return pop_new

