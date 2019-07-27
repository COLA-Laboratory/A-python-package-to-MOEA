import numpy as np
import operator
import functools

class DTLZ1():
    def __init__(self,D,M):
        self.D = D
        self.M = M
        self.lower = np.zeros(self.D)
        self.upper = np.ones(self.D)

    def evaluate(self,x):
        k = self.D-self.M+1
        sum1 = 0
        for i in range(k):
            sum1+= (x[self.M-1+i]-0.5)**2 - np.cos(20*np.pi*(x[self.M-1+i]-0.5))
        g = 100*(k+sum1)
        obj = [0.5*(1.0+g)]*self.M #就是变成了一个self.M的list


        #这个地方是一个连乘，好好理解一下就OK

        for i in range(self.M):
            obj[i] *= functools.reduce(operator.mul,
                                       [x for x in x[:self.M-i-1]],1
                                       )
            if i>0:
                obj[i]*= 1- x[self.M-i-1]

        return obj


class DTLZ2():
    def __init__(self,D,M):
        self.D = D
        self.M = M
        self.lower = np.zeros(self.D)
        self.upper = np.ones(self.D)

    def evaluate(self,x):
        k = self.D - self.M + 1
        g = 0
        for i in range(k):
            g += (x[self.M-1+i]-0.5)**2
        obj = [1+g]*self.M

        for i in range(self.M):
            obj[i]*=functools.reduce(operator.mul,
                                     [np.cos(x*np.pi/2) for x in x[:self.M-i-1]],1
                                     )
            if i>0:
                obj[i]*=np.sin(x[self.M-i-1]*np.pi*0.5)

        return obj


class DTLZ3():
    def __init__(self,D,M):
        self.D = D
        self.M = M
        self.lower = np.zeros(self.D)
        self.upper = np.ones(self.D)

    def evaluate(self, x):
        k = self.D - self.M + 1
        sum1 = 0
        for i in range(k):
            sum1 += (x[self.M-1+i]-0.5)**2 - np.cos(20*np.pi*(x[self.M-1+i]-0.5))
        g = 100 * (k + sum1)
        obj = [1 + g] * self.M
        for i in range(self.M):
            obj[i] *= functools.reduce(operator.mul,
                                       [np.cos(x * np.pi / 2) for x in x[:self.M - i - 1]], 1
                                       )
            if i > 0:
                obj[i] *= np.sin(x[self.M - i - 1] * np.pi * 0.5)

        return obj


class DTLZ4():
    def __init__(self,D,M):
        self.D = D
        self.M = M
        self.lower = np.zeros(self.D)
        self.upper = np.ones(self.D)

    def evaluate(self,x):
        k = self.D - self.M + 1
        g = 0
        for i in range(k):
            g += (x[self.M - 1 + i] - 0.5) ** 2
        obj = [1 + g] * self.M

        for i in range(self.M):
            obj[i] *=functools.reduce(operator.mul,
                                      [np.cos(0.5*np.pi*(x**100)) for x in x[:self.M-1-i]],1
                                      )
            if i>0:
                obj[i]*=np.sin((x[self.M-i-1])**100 * 0.5 * np.pi)
        return obj


class DTLZ5():
    def __init__(self,D,M):
        self.D = D
        self.M = M
        self.lower = np.zeros(self.D)
        self.upper = np.ones(self.D)


    def evaluate(self,x):
        k = self.D -self.M + 1
        g = 0
        for i in range(k):
            g += (x[self.M - 1 + i] - 0.5) ** 2
        obj = [1 + g] * self.M


        theta = []
        for i in range(self.M):
            if i == 0:
                theta.append(x[0]*np.pi*0.5)
            else:
                temp = np.pi*(1+2*g*x[i])/(4*(1+g))
                theta.append(temp)



        for i in range(self.M):
            obj[i]*=functools.reduce(operator.mul,
                                     [np.cos(theta) for theta in theta[:self.M-1-i]],1
                                     )
            if i > 0:
                obj[i]*=np.sin(theta[self.M-1-i])


        return obj



class DTLZ7():
    def __init__(self,D,M):
        self.D = D
        self.M = M
        self.lower = np.zeros(self.D)
        self.upper = np.ones(self.D)

    def evaluate(self,x):

        k = self.D - self.M + 1
        obj = x[:self.M-1]
        g = 1.0 + (9.0 * sum(x[self.D - k:])) / k
