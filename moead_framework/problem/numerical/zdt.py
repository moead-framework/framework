import numpy as np
import random

from moead_framework.problem.problem import Problem
from moead_framework.solution.one_dimension_solution import OneDimensionSolution


class Zdt1(Problem):
    """
    Implementation of the Zdt1 problem.
    https://sop.tik.ee.ethz.ch/download/supplementary/testproblems/zdt1/index.php

    E. Zitzler, K. Deb, and L. Thiele. Comparison of Multiobjective Evolutionary Algorithms: Empirical Results. Evolutionary Computation, 8(2):173-195, 2000
    """

    def __init__(self, size):
        """
        Constructor of the problem

        :param size: {integer} number of variables in a solution
        """
        self.n = size
        super().__init__()

    def f(self, function_id, solution):
        x = solution[:]

        if function_id == 0:
            return x[0]
        else:
            g = 1 + 9.0 / (self.n - 1) * np.sum(x[1:])
            return g * (1 - np.power((x[0] / g), 0.5))

    def generate_random_solution(self, evaluate=True):
        solution = []
        for i in range(0, self.n):
            solution.append(random.random())

        return self.generate_solution(solution)

    def generate_solution(self, array, evaluate=True):
        x = OneDimensionSolution(array)

        for j in range(self.number_of_objective):
            if evaluate:
                x.F.append(self.f(j, x.solution))
            else:
                x.F.append(None)

        return x
