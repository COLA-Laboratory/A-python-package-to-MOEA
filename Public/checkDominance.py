def checkDominance(individual1,individual2):
    flag1 = 0
    flag2 = 0
    for i in range(individual1.problem.M):

        if(individual1.obj[i] < individual2.obj[i]):
            flag1 = 1
        elif(individual2.obj[i] < individual1.obj[i]):
            flag2 = 1
    if(flag1 == 1 and flag2 == 0):

        return 1
    elif(flag1 == 0 and flag2 == 1):

        return -1
    else:
        return 0