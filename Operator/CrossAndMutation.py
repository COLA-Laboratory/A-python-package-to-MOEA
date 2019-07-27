import random
import  numpy as np
from Public.Individual import Individual


def crossMutation(pop_parent,  D, lower, upper, pc, pm ,problem, yita1= 20, yita2 = 20):
    # 模拟二进制交叉和多项式变异
    pop_offspring = []
    # 随机选两个父代个体
    for i in range(round(len(pop_parent) / 2)):
        parent_1 = round(len(pop_parent) * random.random())
        if (parent_1 == len(pop_parent)):
            parent_1 = len(pop_parent) - 1
        parent_2 = round(len(pop_parent) * random.random())
        if (parent_2 == len(pop_parent)):
            parent_2 = len(pop_parent) - 1
        while (parent_1 == parent_2):
            parent_1 = round(len(pop_parent) * random.random())
            if (parent_1 == len(pop_parent)):
                parent_1 = len(pop_parent) - 1
        # 随机得到两个不相等的索引，然后选取个体
        parent1 = pop_parent[parent_1]
        parent2 = pop_parent[parent_2]
        off1 = parent1
        off2 = parent2
        if (random.random() < pc):
            # 初始化子代种群
            off1x = []
            off2x = []
            # 模拟二进制交叉
            for j in range(D):
                if random.random() <= 0.5:
                    if (np.fabs(parent1.x[j] - parent2.x[j]) > 1e-9):
                        if (parent1.x[j] < parent2.x[j]):
                            y1 = parent1.x[j]
                            y2 = parent2.x[j]
                        else:
                            y1 = parent2.x[j]
                            y2 = parent1.x[j]
                        rand = random.random()
                        yl = lower[j]
                        yu = upper[j]
                        beta = 1.0 + (2.0 * (y1 - yl) / (y2 - y1))
                        alpha = 2.0 - pow(beta, -(yita1 + 1.0))
                        if (rand <= (1.0 / alpha)):
                            betaq = pow((rand * alpha), (1.0 / (yita1 + 1.0)))
                        else:
                            betaq = pow((1.0 / (2.0 - rand * alpha)), (1.0 / (yita1 + 1.0)))

                        off11 = 0.5 * ((y1 + y2) - betaq * (y2 - y1))
                        beta = 1.0 + (2.0 * (yu - y2) / (y2 - y1))
                        alpha = 2.0 - pow(beta, -(yita1 + 1.0))
                        if (rand <= (1.0 / alpha)):
                            betaq = pow((rand * alpha), (1.0 / (yita1 + 1.0)))
                        else:
                            betaq = pow((1.0 / (2.0 - rand * alpha)), (1.0 / (yita1 + 1.0)))
                        off22 = 0.5 * ((y1 + y2) + betaq * (y2 - y1))
                        # 使子代在定义域内
                        if (off11 > upper[j]):
                            off11 = upper[j]
                        elif (off11 < lower[j]):
                            off11 = lower[j]
                        if (off22 > upper[j]):
                            off22 = upper[j]
                        elif (off22 < lower[j]):
                            off22 = lower[j]
                        if random.random() <= 0.5:
                            off1x.append(off22)
                            off2x.append(off11)
                        else:
                            off1x.append(off11)
                            off2x.append(off22)
                    else:
                        off1x.append(parent1.x[j])
                        off2x.append(parent2.x[j])
                else:
                    off1x.append(parent1.x[j])
                    off2x.append(parent2.x[j])
            off1 = Individual(off1x,problem)
            off2 = Individual(off2x,problem)

        # 多项式变异
        off1x = []
        off2x = []
        for j in range(D):
            if (random.random() < pm):
                y1 = off1.x[j]
                y2 = off2.x[j]
                ylow = lower[j]
                yu = upper[j]
                delta11 = (y1 - ylow) / (yu - ylow)
                delta12 = (yu - y1) / (yu - ylow)
                delta21 = (y2 - ylow) / (yu - ylow)
                delta22 = (yu - y2) / (yu - ylow)
                rnd = random.random()
                mut_pow = 1.0 / (yita2 + 1.0)
                if (rnd <= 0.5):
                    xy1 = 1.0 - delta11;
                    xy2 = 1.0 - delta21;
                    val1 = 2.0 * rnd + (1.0 - 2.0 * rnd) * (pow(xy1, (yita2 + 1.0)));
                    val2 = 2.0 * rnd + (1.0 - 2.0 * rnd) * (pow(xy2, (yita2 + 1.0)));
                    deltaq1 = pow(val1, mut_pow) - 1.0
                    deltaq2 = pow(val2, mut_pow) - 1.0
                else:
                    xy1 = 1.0 - delta12;
                    xy2 = 1.0 - delta22;
                    val1 = 2.0 * (1.0 - rnd) + 2.0 * (rnd - 0.5) * (pow(xy1, (yita2 + 1.0)));
                    val2 = 2.0 * (1.0 - rnd) + 2.0 * (rnd - 0.5) * (pow(xy2, (yita2 + 1.0)));

                    deltaq1 = 1.0 - (pow(val1, mut_pow));
                    deltaq2 = 1.0 - (pow(val2, mut_pow))

                off11 = float(off1.x[j] + deltaq1 * (upper[j] - lower[j]))
                off22 = float(off2.x[j] + deltaq2 * (upper[j] - lower[j]))
                if (off11 > upper[j]):
                    off11 = upper[j]
                elif (off11 < lower[j]):
                    off11 = lower[j]
                if (off22 > upper[j]):
                    off22 = upper[j]
                elif (off22 < lower[j]):
                    off22 = lower[j]
                off1x.append(off11)
                off2x.append(off22)
            else:
                off1x.append(off1.x[j])
                off2x.append(off2.x[j])
        off1 = Individual(off1x,problem)
        off2 = Individual(off2x,problem)
        pop_offspring.append(off1)
        pop_offspring.append(off2)
    return pop_offspring