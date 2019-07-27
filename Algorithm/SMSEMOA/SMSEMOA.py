from Public.InitialPop import initial
from Public.checkDominance import checkDominance
from Operator.CrossAndMutation import crossMutation
from Algorithm.SMSEMOA.Reduce import Reduce
from DrawFunction.Draw import draw
from Metric.HV import HV

import numpy as np
import matplotlib.pyplot as plt
import time

def SMSEMOA(N,maxgen,problem,encoding):
    D = problem.D
    M = problem.M
    lower = problem.lower
    upper = problem.upper

    pc = 1
    pm = 1 / D

    pop = initial(N, D, M, lower, upper, problem, encoding)
    gen = 1

    start = time.time()
    fig = plt.figure()
    while gen <= maxgen:
        for i in range(N):
            k = np.random.randint(0, len(pop))
            l = np.random.randint(0, len(pop))

            # keep different
            while k == l:
                l = np.random.randint(0, len(pop))

            pop_parent = [pop[k], pop[l]]
            pop_offspring = crossMutation(pop_parent,D,lower,upper,pc,pm,problem)
            if checkDominance(pop_offspring[0], pop_offspring[1]):
                q = pop_offspring[0]
            else:
                q = pop_offspring[1]

            pop_combine = np.hstack([pop,q])
            pop_combine = list(pop_combine)
            pop = Reduce(pop_combine,M)

        gen += 1
        #start1 = time.time()
        draw(problem,pop, M, fig)
        if gen < maxgen:
            plt.clf()
        #end1 = time.time()
        #print("3：%7fs" % (end1 - start1))

        if (gen % 10) == 0:
            print("%d gen has completed!\n" % gen)

    plt.ioff()
    end = time.time()
    print("runtime：%2fs" % (end - start))
    #plt.show()
    # PRINT INDICATOR


    score = HV(pop)

    print("HV indicator:%f" % score)

    plt.show()