import numpy as np

def Calfitness(pop,kappa,N):
    temp = []
    for i in range(N):
       temp.append(pop[i].obj)

    popObj = np.vstack(temp)


    minObj = np.min(popObj,0)
    minObj = np.tile(minObj,(N,1))
    maxObj = np.max(popObj,0)
    maxObj = np.tile(maxObj,(N,1))

    #标准化
    popObj = (popObj-minObj)/(maxObj-minObj)
    I = np.zeros((N,N))

    for i in range(N):
        for j in range(N):
            I[i][j] = np.max(popObj[i,:]-popObj[j,:])

    C = np.max(np.abs(I))
    C = np.tile(C,(N,N))
    fitness = np.exp(-I/C/kappa)
    Fitness = np.sum(np.exp(-I/C/kappa),0)-1

    for i in range(N):
        pop[i].fitness = Fitness[i]
    return Fitness,fitness,pop
