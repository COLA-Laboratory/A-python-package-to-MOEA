from Public.InitialPop import initial
from Algorithm.NSGAII.Non_Dominated_Sort import nonDominatedSort
from Algorithm.NSGAII.CrowdingDistance import crowdingDistance
from Algorithm.NSGAII.NSGAIISelection import tournamentSelection,elitism
from Operator.CrossAndMutation import crossMutation
from DrawFunction.Draw import draw

import matplotlib.pyplot as plt
import time

from Metric.HV import HV


def NSGAII(N,maxgen,problem,encoding):
    D = problem.D
    M = problem.M
    lower = problem.lower
    upper = problem.upper
    pc = 0.9
    pm = 1/D
    pop = initial(N, D, M, lower, upper, problem, encoding)

    F1, pop_non,_ = nonDominatedSort(N, pop)
    pop = crowdingDistance(F1, pop_non, M)

    start = time.time()
    gen = 1
    fig = plt.figure()
    plt.ion()
    while gen <= maxgen:

        pop_parent1 = tournamentSelection(pop, N)
        pop_parent2 = tournamentSelection(pop, N)
        pop_parent = pop_parent1 + pop_parent2
        #print(np.size(pop_parent))
        pop_offspring = crossMutation(pop_parent, D, lower, upper, pc, pm,  problem)
        pop_combine = pop + pop_offspring

        F, pop_combine_non,_= nonDominatedSort(len(pop_combine), pop_combine)
        pop_combine2 = crowdingDistance(F, pop_combine_non, M)

        pop = elitism(N, pop_combine2)

        draw(problem,pop, M,fig)
        if gen <maxgen:
             plt.clf()


        if (gen % 10) == 0:
            print("%d gen has completed!\n" % gen)
        gen = gen + 1;
    end = time.time()
    plt.ioff()

    print("runtime：%2fs" % (end - start))


    #PRINT INDICATOR


    score = HV(pop)

    print("HV indicator:%f" % score)


    plt.show()










