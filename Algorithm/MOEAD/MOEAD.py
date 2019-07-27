from Public.FindNeighbour import FindNeighbour
from Public.UniformPoint import UniformPoint
from Public.BestValue import Best
from Public.InitialPop import initial
from Algorithm.MOEAD.DecomposeMethod import Tchebycheff
from Operator.CrossAndMutation import crossMutation
from Public.checkDominance import checkDominance
from DrawFunction.Draw import draw

import time
import numpy as np
import matplotlib.pyplot as plt


from Metric.HV import HV



def MOEAD(N,maxgen,problem,encoding,type = 1):
    start = time.time()


    D = problem.D
    M = problem.M
    lower = problem.lower
    upper = problem.upper
    pc = 1
    pm = 1 / D

    W, N = UniformPoint(N, M)
    T = np.ceil(N/10)
    T = int(T)
    B = FindNeighbour(W, N, M, T)

    #print(W[99])



    pop = initial(N, D, M, lower, upper, problem, encoding)
    z = Best(pop)

    gen = 1
    plt.ion()
    fig = plt.figure()

    while gen<=maxgen:
        for i in range(N):
            k = np.random.randint(0,T)
            l = np.random.randint(0,T)
            while k==l:
                l = np.random.randint(0,T)
            pop_parent = [pop[B[i][k]],pop[B[i][l]]]
            pop_offspring = crossMutation(pop_parent, D, lower, upper, pc, pm, problem)
            if checkDominance(pop_offspring[0],pop_offspring[1]):
                y = pop_offspring[0]
            else:
                y = pop_offspring[1]

            for j in range(len(z)):
                if y.obj[j]<z[j]:
                    z[j] = y.obj[j]

            #小心这使用的权重，之前搞错了
            for j in range(T):
                if Tchebycheff(y,W[B[i][j]],z) < Tchebycheff(pop[B[i][j]],W[B[i][j]],z):
                    pop[B[i][j]] = y


        draw(problem,pop, M, fig)
        # print(Tchebycheff(pop[99],W[99],z))
        # print(pop[99].obj[0],pop[99].obj[1])
        if gen < maxgen:
            plt.clf()

        if (gen % 10) == 0:
            print("%d gen has completed!\n" % gen)
        gen = gen + 1;
    end = time.time()
    plt.ioff()
    print("runtime：%2fs" % (end - start))
    # for i in range(N):
    #     print("population %f obj[0]: %f obj[1]: %f obj[2]: %f"%(i,pop[i].obj[0],pop[i].obj[1],pop[i].obj[2]))
    #     print("x[0]:%f x[1]:%f x[2]:%f x[3]:%f x[4]:%f x[5]:%f  x[6]:%f x[7]:%f x[8]:%f"
    #           %(pop[i].x[0],pop[i].x[1],pop[i].x[2],pop[i].x[3],pop[i].x[4],pop[i].x[5],pop[i].x[6],pop[i].x[7],pop[i].x[8])
    #           )
    #     print("here")

    # PRINT INDICATOR

    score = HV(pop)

    print("HV indicator:%f" % score)




    plt.show()
    #drawStationary(pop,M)

