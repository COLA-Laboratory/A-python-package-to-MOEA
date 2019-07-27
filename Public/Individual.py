class Individual():

    def __init__(self, x, problem):
        self.x = x
        self.problem = problem
        self.obj = self.problem.evaluate(x)
        self.fitness = 0
        self.cd = 0
        self.paretoRank = 0