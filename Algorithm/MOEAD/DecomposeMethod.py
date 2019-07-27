import numpy as np


def Tchebycheff(individual,weight,z):
    temp = []
    for i in range(len(individual.obj)):
        temp.append(weight[i]*np.abs(individual.obj[i]-z[i]))

    return np.max(temp)
