import numpy as np
from Public.checkDominance import checkDominance


def TournamentSelection(pop,N):




    pop_new = []
    tournament = 2
    a = round(N/2)
    pop_candidate = np.zeros(tournament)
    pop_fitness = np.zeros(tournament)

    for i in range(a):
        for j in range(tournament):
            pop_candidate[j] = int(np.floor(N*np.random.rand()))
        while(pop_candidate[0]==pop_candidate[1]):
            pop_candidate[0] = int(np.floor(N*np.random.rand()))


        result = checkDominance(pop[int(pop_candidate[0])],pop[int(pop_candidate[1])])
        if result == 1:
            pop_new.append(pop[int(pop_candidate[0])])
            #print("here")
        elif result == -1:
            pop_new.append(pop[int(pop_candidate[1])])
        else:
            for j in range(tournament):
                pop_fitness[j] = pop[int(pop_candidate[j])].fitness

            index = np.argmin(pop_fitness)
            #print(pop_candidate[index])
            pop_new.append(pop[int(pop_candidate[index])])

    return pop_new