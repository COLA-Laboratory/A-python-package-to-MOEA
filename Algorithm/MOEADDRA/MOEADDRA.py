from Public.InitialPop import initial
from Public.UniformPoint import UniformPoint
from Public.BestValue import Best
from Public.FindNeighbour import FindNeighbour
from Algorithm.MOEADDRA.MOEADDRAselection import MOEADDRAselection
from Operator.DE import DEandMuation
from Algorithm.MOEAD.DecomposeMethod import Tchebycheff
from DrawFunction.Draw import draw

import matplotlib.pyplot as plt

import numpy as np
import time

from Metric.HV import HV


def MOEADDRA(N,maxgen,problem,encoding):
    start = time.time()
    D = problem.D
    M = problem.M
    lower = problem.lower
    upper = problem.upper

    CR = 1
    pm = 1/D
    delta = 0.9
    F = 0.5
    nr = np.ceil(0.01*N)

    W,N = UniformPoint(N, M)
    T = round(N/10)
    pop = initial(N, D, M, lower, upper, problem, encoding)
    B = FindNeighbour(W, N, M, T)
    z = Best(pop)

    utility = [1]*N
    Delta = np.zeros(N)
    oldFunction = np.zeros(N)


    fig = plt.figure()
    plt.ion()
    gen = 0
    #print("here!!!")
    while gen < maxgen:
        for i in range(5):
            I = MOEADDRAselection(utility,W,N,M)
            #print("here!")
            for i in range(len(I)):
                rand = np.random.rand()
                if(rand<delta):
                    P = B[int(I[i])]
                else:
                    P = [j for j in range(N)]


                k = np.random.randint(0, len(P))
                l = np.random.randint(0, len(P))


                y = DEandMuation(pop[int(I[i])],pop[P[k]],pop[P[l]],problem,CR, F,pm)
                for j in range(len(z)):
                    if y.obj[j] < z[j]:
                        z[j] = y.obj[j]

                c = 0
                #flag = np.zeros(len(P))
                while(c<nr and len(P)!=0):

                    j = np.random.randint(0,len(P))

                    if Tchebycheff(y,W[P[j]],z) < Tchebycheff(pop[P[j]],W[P[j]],z):
                        #print("here!")
                        pop[P[j]] = y
                        c = c+1
                    P = np.delete(P,j)
                        #P.remove(j)
                        #print(c)

        if gen%20 == 0:
            if gen != 0:
                for j in range(N):
                    Delta[j] = (oldFunction[j] - Tchebycheff(pop[j],W[j],z))/oldFunction[j]

                    if Delta[j] > 0.001:
                       # print("yes")
                        utility[j] = 1
                    else:
                        #print("no")
                        utility[j] = (0.95 + 0.05*Delta[j]/0.001) * utility[j]
            for i in range(N):
                oldFunction[i] = Tchebycheff(pop[i],W[i],z)

        draw(problem,pop, M, fig)
        if gen < maxgen-1:
            plt.clf()

        if ((gen+1) % 10) == 0:
            print("%d gen has completed!\n" % (gen+1))
        gen = gen + 1;
    end = time.time()
    print("runtime: %.2fs" % (end - start))
    plt.ioff()

    # PRINT INDICATOR


    score = HV(pop)

    print("HV indicator:%f" % score)


    plt.show()




