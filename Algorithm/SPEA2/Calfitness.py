from Public.checkDominance import checkDominance



def Calfitness(pop_combine,k,M):
    Sp = {}  #存储各个解 支配别的解的个数
    Np = {}  #存储支配这个解的 解
    for i in range(len(pop_combine)):
        Sp[i] = 0
        Np[i] = []

        for j in range(len(pop_combine)):
            result = checkDominance(pop_combine[i],pop_combine[j])
            if result == 1:
                Sp[i] +=1
            elif result == -1:
                Np[i].append(j)


    R = []
    for i in range(len(pop_combine)):
        temp = 0
        for j in range(len(Np[i])):
            temp += Sp[Np[i][j]]

        R.append(temp)

    Distance = []
    for i in range(len(pop_combine)):
        distance = []

        for j in range(len(pop_combine)):
            temp = 0

            for k in range(M):
                temp += (pop_combine[i].obj[k] - pop_combine[j].obj[k]) ** 2

            distance.append(temp ** 0.5)

        Distance.append(distance)

    D = []
    for i in range(len(pop_combine)):
        Distance[i].sort()
        D.append(1/(Distance[i][k]+2))

    Fitness = []

    for i in range(len(pop_combine)):
        Fitness.append(R[i]+D[i])
        pop_combine[i].fitness = R[i] + D[i]

    return pop_combine
