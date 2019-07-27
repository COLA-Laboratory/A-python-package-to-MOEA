import numpy as np


def HV(pop,flag = None):

    temp = []
    for i in range(len(pop)):
        temp.append(pop[i].obj)

    popObj = np.vstack(temp)


    N, M = np.shape(popObj)
    # fmin = np.minimum(np.min(popObj,0),np.zeros(M))
    # fmax = np.max(PF,0)*1.1
    # popObj = (popObj-np.tile(fmin,(N,1)))/np.tile(fmax-fmin,(N,1))
    if flag == None:
        refPoint = np.max(popObj, 0)
    else:
        refPoint = np.max(popObj * 1.1, 0)
    if len(popObj) == 0:
        score = 0
    else:
        pl = sorted(popObj, key=lambda x: x[0])
        pl = np.array(pl)
        temp = [1]
        temp.append(pl)
        S = [temp]
        for k in range(M - 1):
            S_ = []
            for i in range(len(S)):
                Stemp = Slice(S[i][1], k, refPoint)
                for j in range(len(Stemp)):
                    temp = []
                    temp.append(Stemp[j][0] * S[i][0])  # depth
                    temp.append(Stemp[j][1])
                    S_.append(temp)
            S = S_
        score = 0
        for i in range(len(S)):
            p = Head(S[i][1])  # 里面是排序好的，直接取
            score = score + S[i][0] * np.abs(p[M - 1] - refPoint[M - 1])
    return score


def Slice(pl, k, refPoint):
    p = Head(pl)
    pl = Tail(pl)
    ql = []
    S = []
    while len(pl) != 0:
        temp = []
        ql = Insert(p, k + 1, ql)  # 把p插入到ql里去，剔除ql中所有被p支配的点，并且保持在k+1维的排序
        p_ = Head(pl)
        temp.append(np.abs(p[k] - p_[k]))  # depth
        temp.append(ql)
        S.append(temp)
        p = p_
        pl = Tail(pl)

    temp = []
    ql = Insert(p, k + 1, ql)
    temp.append(np.abs(p[k] - refPoint[k]))
    temp.append(ql)
    S.append(temp)

    return S


def Insert(p, k, pl):
    flag1 = 0
    flag2 = 0
    ql = []
    hp = Head(pl)
    while len(pl) != 0 and hp[k] < p[k]:
        ql.append(hp)
        # 更新 pl ，hp，继续循环
        pl = Tail(pl)
        hp = Head(pl)
    ql.append(p)
    m = len(p)  # 目标维度
    while len(pl) != 0:
        q = Head(pl)
        # 判断在k维之后p是否支配之前的ql
        for i in range(k, m):
            if p[i] < q[i]:
                flag1 = 1
            elif p[i] > q[i]:
                flag2 = 1

        if ~(flag1 == 1 and flag2 == 0):
            ql.append(Head(pl))
        pl = Tail(pl)

    return ql


def Head(pl):
    if len(pl) == 0:
        p = []
    else:
        p = pl[0]
    return p



def Tail(pl):
    if len(pl) < 2:
        ql = []
    else:
        ql = pl[1:] #返回除去第一行的所有
    return ql