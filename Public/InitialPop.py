import random
from Public.Individual import Individual


def initial(N,D,M,lower,upper,problem,encoding):

    if encoding == 'real':
        p = []
        for i in range(N):
            tempDecVar = []
            for j in range(D):
                tempX = lower[j]+(upper[j]-lower[j])*random.random()
                tempDecVar.append(tempX)
            p.append(Individual(tempDecVar, problem))
        return p
    elif encoding == 'binary':
        #  To do.....


        pass
    elif encoding == 'permutation':
        # To do.....


        pass