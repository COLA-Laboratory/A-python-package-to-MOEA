import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def draw(problem,pop, M,  fig = None, ax = None):
    # ------------------------画图对比--------------------------
    x = []
    y = []
    z = []
    #PF = problem.PF(200)
    if M == 2:
        for i in range(len(pop)):
            x.append(pop[i].obj[0])
            y.append(pop[i].obj[1])
        #plt.plot(PF[:,0],PF[:,1], label='PF',linewidth='0.7', alpha = 0.7, color = 'black')
        #plt.legend()
        plt.scatter(x, y, marker='o', color='#0139DD', s=17)

        plt.xlabel('f1')
        plt.ylabel('f2')
        #plt.show()
        plt.draw()
        plt.pause(0.003)
    elif M == 3:
        for i in range(len(pop)):
            x.append(pop[i].obj[0])
            y.append(pop[i].obj[1])
            z.append(pop[i].obj[2])
        #fig = plt.figure()
        ax = Axes3D(fig)
        ax.scatter(x, y, z, c='#0139DD',s=22)
        ax.view_init(elev=40, azim=40)
        #plt.show()
        plt.draw()
        plt.pause(0.003)
    elif M > 3:
        label = list(range(1, M+1))
        for i in range(len(pop)):
            plt.plot(label, pop[i].obj, c='#3B6575', linewidth='1.2')

        plt.draw()
        plt.pause(0.003)


