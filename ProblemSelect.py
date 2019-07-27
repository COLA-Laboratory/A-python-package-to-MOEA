import TestProblem.ZDT as ZDT
import TestProblem.DTLZ as DTLZ

def problemSelect(problemName,D,M ):
    if problemName=='ZDT1':
        problem = ZDT.ZDT1(D)
    elif problemName == 'ZDT2':
        problem = ZDT.ZDT2(D)
    elif problemName == 'ZDT3':
        problem = ZDT.ZDT3(D)
    elif problemName == 'ZDT4':
        problem = ZDT.ZDT4(D)
    elif problemName == 'ZDT5':
        problem = ZDT.ZDT5(D)
    elif problemName == 'ZDT6':
        problem = ZDT.ZDT6(D)
    elif problemName == 'DTLZ1':
        if M == 0:
            problem = DTLZ.DTLZ1(D, 3)
        else:
            problem = DTLZ.DTLZ1(D, M)
    elif problemName == 'DTLZ2':
        if M == 0:
            problem = DTLZ.DTLZ2(D, 3)
        else:
            problem = DTLZ.DTLZ2(D, M)
    elif problemName == 'DTLZ3':
        if M == 0:
            problem = DTLZ.DTLZ3(D, 3)
        else:
            problem = DTLZ.DTLZ3(D, M)
    elif problemName == 'DTLZ4':
        if M == 0:
            problem = DTLZ.DTLZ4(D, 3)
        else:
            problem = DTLZ.DTLZ4(D, M)
    elif problemName == 'DTLZ5':
        if M == 0:
            problem = DTLZ.DTLZ5(D, 3)
        else:
            problem = DTLZ.DTLZ5(D, M)



    return problem