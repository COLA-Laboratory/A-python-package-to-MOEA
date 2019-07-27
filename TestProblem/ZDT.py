import numpy as np


class ZDT1():
    def __init__(self,D):
        self.M = 2
        self.D = D
        self.lower = np.zeros(self.D)
        self.upper = np.ones(self.D)

    def evaluate(self,x):
        obj1 = x[0]
        g = 1+9*sum(x[1:self.D])/(self.D-1)
        h = 1-(obj1/g)**0.5
        obj2 = g*h
        obj = [obj1, obj2]
        return obj

    def PF(self,N):
        P = np.zeros((N,self.M))
        P[:, 0] = np.arange(0,1+1/N,1/(N-1))
        P[:, 1] = 1-P[:,0]**0.5
        return P




class ZDT2():
    def __init__(self,D):
        self.M = 2
        self.D = D
        self.lower = np.zeros(self.D)
        self.upper = np.ones(self.D)

    def evaluate(self,x):
        obj1 = x[0]
        g = 1+9*sum(x[2:self.D])/(self.D-1)
        h = 1-(obj1/g)**2
        obj2 = g*h
        obj = [obj1, obj2]
        return obj

    def PF(self,N):
        P = np.zeros((N,self.M))
        P[:, 0] = np.arange(0,1+1/N,1/(N-1))
        P[:, 1] = 1-P[:,0]**2
        return P

class ZDT3():
    def __init__(self,D):
        self.M = 2
        self.D = D
        self.lower = np.zeros(self.D)
        self.upper = np.ones(self.D)

    def evaluate(self,x):
        obj1 = x[0]
        g = 1+9*sum(x[1:self.D])/(self.D-1)
        h = 1-(obj1/g)**0.5-(obj1/g)*np.sin(10*np.pi*obj1)
        obj2 = g*h
        obj = [obj1,obj2]
        return obj


class ZDT4():
    def __init__(self,D):
        self.M = 2
        self.D = D
        self.lower = np.hstack([0, np.zeros(self.D-1)-5])
        self.upper = np.hstack([1, np.zeros(self.D-1)+5])

    def evaluate(self,x):
        obj1 = x[0]
        sum1 = 0
        for i in range(self.D - 1):
            sum1 = sum1 + (x[i + 1]) ** 2 - 10 * np.cos(4 * np.pi * x[i + 1])
        g =1 + 10*(self.D-1) + sum1
        h = 1-(obj1/g)**0.5
        obj2 = g*h
        obj = [obj1, obj2]
        return obj


class ZDT5():
    pass


class ZDT6():
    def __init__(self,D):
        self.M = 2
        self.D = D
        self.lower = np.zeros(self.D)
        self.upper = np.ones(self.D)

    def evaluate(self,x):
        obj1 = 1 - np.exp(-4*x[0])*(np.sin(6*np.pi*x[0])**6)
        g = 1+9*(sum(x[1:self.D])/(self.D-1))**0.25
        h = 1-(obj1/g)**2
        obj2 = g*h
        obj = [obj1,obj2]
        return obj

