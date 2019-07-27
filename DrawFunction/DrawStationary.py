import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def drawStationary(pop,M,fig = None):
    # ------------------------画图对比--------------------------
    x = []
    y = []
    z = []
    if M == 2:
        for i in range(len(pop)):
            x.append(pop[i].obj[0])
            y.append(pop[i].obj[1])
        plt.scatter(x, y, marker='o', color='red', s=10)
        plt.xlabel('f1')
        plt.ylabel('f2')
        plt.show()

    elif M == 3:
        for i in range(len(pop)):
            x.append(pop[i].obj[0])
            y.append(pop[i].obj[1])
            z.append(pop[i].obj[2])
        fig = plt.figure()
        ax = Axes3D(fig)
        ax.scatter(x, y, z, c='r')
        ax.view_init(elev=30, azim=30)
        plt.show()

