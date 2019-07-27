def Best(P):
    best = []
    for i in range(len(P[0].obj)):
        best.append(P[0].obj[i])
    for i in range(len(P)):
        for j in range(len(P[i].obj)):
            if P[i].obj[j] < best[j]:
                best[j] = P[i].obj[j]
    return best

