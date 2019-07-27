

import numpy as np

def MatingSelection(pop_ex,N):

    pop_mating = []
    for i in range(N):
        k = np.random.randint(0, len(pop_ex))
        l = np.random.randint(0, len(pop_ex))
        while k==l:
            l = np.random.randint(0, len(pop_ex))


        if pop_ex[k].fitness <= pop_ex[l].fitness:

            pop_mating.append(pop_ex[k])
        else:

            pop_mating.append(pop_ex[l])


    return pop_mating




