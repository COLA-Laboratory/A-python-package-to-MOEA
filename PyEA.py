from Algorithm.NSGAII.NSGAII import NSGAII
from Algorithm.MOEAD.MOEAD import MOEAD
from Algorithm.IBEA.IBEA import IBEA
from ProblemSelect import problemSelect
from Algorithm.MOEADDRA.MOEADDRA import MOEADDRA
from Algorithm.SMSEMOA.SMSEMOA import SMSEMOA
from Algorithm.SPEA2.SPEA2 import SPEA2


def PyEA(problemName,algorithm,N,maxgen,encoding,D,M=0):
    problemInstance = problemSelect(problemName,D,M)
    if algorithm == 'NSGAII':
        NSGAII(N, maxgen, problemInstance, encoding)
    elif algorithm == 'MOEAD':
        MOEAD(N, maxgen, problemInstance, encoding)
    elif algorithm == 'IBEA':
        IBEA(N,maxgen, problemInstance, encoding)
    elif algorithm == 'MOEADDRA':
        MOEADDRA(N,maxgen, problemInstance, encoding)
    elif algorithm == 'SMSEMOA':
        SMSEMOA(N,maxgen, problemInstance, encoding)
    elif algorithm == 'SPEA2':
        SPEA2(N,maxgen, problemInstance, encoding)