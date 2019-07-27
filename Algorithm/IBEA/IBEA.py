from Public.InitialPop import initial
from Algorithm.IBEA.Calfitness import Calfitness
from Algorithm.IBEA.TournamentSelection import TournamentSelection
from Algorithm.IBEA.EnvironmentSelection import EnviromentSelection


from Operator.CrossAndMutation import crossMutation
from DrawFunction.Draw import draw
import time
import matplotlib.pyplot as plt
import numpy as np

from Metric.HV import HV


def IBEA(N,maxgen,problem,encoding):
    start = time.time()
    D = problem.D
    M = problem.M
    lower = problem.lower
    upper = problem.upper

    pc = 1
    pm = 1/D

    kappa = 0.05

    pop = initial(N,D,M,lower,upper,problem,encoding)

    gen = 1


    plt.ion()
    fig = plt.figure()
    while gen<=maxgen:
        Fitness,fitness,pop = Calfitness(pop,kappa,len(pop))
        pop_parent1 = TournamentSelection(pop,N)
        pop_parent2 = TournamentSelection(pop,N)
        pop_parent = pop_parent1+pop_parent2
        length = len(pop_parent)
        pop_offspring = crossMutation(pop_parent,D,lower,upper,pc,pm,problem,1,2)
        pop_mixed = pop + pop_offspring
        Fitness,fitness,pop = Calfitness(pop_mixed,kappa,len(pop_mixed))

        pop = EnviromentSelection(pop_mixed,fitness,length)



        draw(problem,pop,M,fig)
        if gen < maxgen:
            plt.clf()

        if gen%10 == 0:
            print("%d gen has completed"%gen)
        gen+=1

    end = time.time()

    plt.ioff()
    print("runtime: %.2fs"%(end-start))

    # PRINT INDICATOR
    temp = []
    for i in range(N):
        temp.append(pop[i].obj)

    popObj = np.vstack(temp)

    score = HV(popObj)

    print("HV indicator:%f" % score)

    plt.show()