import numpy as np
from Public.Individual import Individual

def DEandMuation(ind1,ind2,ind3,problem,CR,F,pm,yita = 20):

    y = []
    for i in range(len(ind1.x)):
        if(np.random.rand() <= CR):
            temp = ind1.x[i] + F*(ind2.x[i]-ind3.x[i])
        else:
            tmep = ind1.x[i]

        y.append(temp)

    for i in range(len(y)):

        if(np.random.rand()<=pm):
            ak = problem.lower[i]
            bk = problem.upper[i]

            rand = np.random.rand()
            if(rand<0.5):
                thetak = (2*rand)**(1/1+yita)-1
            else:
                thetak = 1-(2-2*rand)**(1/yita+1)
            y[i] = y[i]+thetak*(bk-ak)



    #Repair
    for i in range(len(y)):
        ak = problem.lower[i]
        bk = problem.upper[i]
        if y[i] > bk :
            y[i] = bk
        elif y[i] < ak:
            y[i] = ak

    return Individual(y,problem)