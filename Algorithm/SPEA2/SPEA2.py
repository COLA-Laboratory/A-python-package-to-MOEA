from Public.InitialPop import initial
from Algorithm.SPEA2.Calfitness import Calfitness
from Algorithm.SPEA2.EnvironmentalSelection import EnvironmentalSelection
from Algorithm.SPEA2.MatingSelection import MatingSelection
from Operator.CrossAndMutation import crossMutation
from DrawFunction.Draw import draw


import numpy as np
import matplotlib.pyplot as plt
import time

def SPEA2(N,maxgen,problem,encoding):
    start = time.time()

    D = problem.D
    M = problem.M
    lower = problem.lower
    upper = problem.upper

    pc = 1
    pm = 1/D
    k = round(np.sqrt(2*N))

    pop = initial(N,D,M,lower,upper,problem,encoding)
    pop_ex = []

    fig = plt.figure()
    plt.ion()
    gen = 1
    while True:
        pop_combine = pop+pop_ex

        pop_combine = Calfitness(pop_combine,k,M)
        pop_ex = EnvironmentalSelection(pop_combine,N,M)

        draw(problem,pop_ex,M,fig)
        if gen <maxgen:
             plt.clf()
        if gen > maxgen:
            break


        pop_mating = MatingSelection(pop_ex,N)
        #print(len(pop_mating))
        pop = crossMutation(pop_mating,D,lower,upper,pc,pm,problem)
        #print("!!%d"%len(pop))

        gen+=1
        if gen %10 == 0:
            print("%d gen has completed"%gen)
    end = time.time()
    plt.ioff()

    print("runtime: %.2fs"%(end-start))
    plt.show()