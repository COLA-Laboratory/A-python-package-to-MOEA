
from Public.checkDominance import checkDominance

def EnvironmentalSelection(pop_combine,N,M):
    pop_ex = []

    for i in range(len(pop_combine)):
        flag = 1
        for j in range(len(pop_combine)):
            if checkDominance(pop_combine[i],pop_combine[j]) == -1:
                flag = 0
        if flag == 1:
            pop_ex.append(pop_combine[i])



    N_ex = len(pop_ex)

    if N_ex == N:
        return pop_ex

    elif N_ex > N:
        Distance  = []
        for i in range(len(pop_ex)):
            distance = []
            for j in range(len(pop_ex)):

                temp = 0
                for k in range(M):

                    temp += (pop_ex[i].obj[k]-pop_ex[j].obj[k]) ** 2
                distance.append(temp ** 0.5)

            Distance.append(distance)

        Distance_rank = []  #每一行单独排序
        for distance in Distance:
            Distance_rank.append(sorted(distance))

        Distance_temp = sorted(Distance_rank, key = lambda x:x[0:N])
        k = N_ex-N
        index = []
        for i in range(k):
            index.append(Distance_rank.index(Distance_temp[0]))    # 注意这的Distance_temp的索引一直是0，取最差的那个
                                                                    # 这里的index是 pop_ex长度并没有改变的时候的index，要注意操作
            Distance[index[i]] = [float("inf")] * len(pop_ex)

            # 更新Distance_rank 和 Distance_temp
            for distance in Distance:
                tmp = index[i]

                distance[tmp] = float("inf")

            Distance_rank = []  # 每一行单独排序
            for distance in Distance:
                Distance_rank.append(sorted(distance))
            Distance_temp = sorted(Distance_rank, key=lambda x: x[0:len(pop_ex)])


        # solution 1
        temp = []
        for i in range(len(pop_ex)):
            if i not in index:

                temp.append(pop_ex[i])




        return temp

    elif N_ex < N:
        pop_ex = []
        pop_temp = sorted(pop_combine, key=lambda x: x.fitness)
        for i in range(N):
            pop_ex.append(pop_temp[i])

        return pop_ex


