import random
import numpy as np
from moead_framework.core.genetic_operator.abstract_operator import GeneticOperator


class Crossover(GeneticOperator):
    """
    Multi-point crossover.

    Require 2 solutions, run a crossover according to the number of points wanted.
    """

    def __init__(self, solutions, crossover_points=1):
        """
        Constructor of the Crossover operator

        :param solutions: list<list<integer>> list of solution's representation (In algorithms, it is represented by the attribute :class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution.decision_vector` of the class :class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`)
        :param crossover_points: {integer} the number of points for the crossover
        """
        super().__init__(solutions)
        if len(self.solutions[0]) <= crossover_points:
            msg = f"The number of crossover points (crossover_points={crossover_points}) must be strictly smaller than the number of variables in the solution (n={len(self.solutions[0])})."
            raise ValueError(msg)
        elif crossover_points == 0:
            msg = f"The number of crossover points (crossover_points={crossover_points}) must be positive."
            raise ValueError(msg)

        self.crossover_points = int(crossover_points)

    def run(self):
        """
        Execute the genetic operator

        :return: {:class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`} the offspring
        """

        self.number_of_solution_is_correct(n=2)
        solution1 = self.solutions[0]
        solution2 = self.solutions[1]

        list_of_points = set()
        while len(list_of_points) < self.crossover_points:
            int_rand = random.randint(1, len(solution1) - 1)
            list_of_points.add(int_rand)

        list_of_points = sorted(list(list_of_points))

        current = 0
        last_i = 0
        child = []
        for i in range(self.crossover_points):
            last_i = i
            if i % 2 == 0:
                child = np.append(child, solution1[current : list_of_points[i]])
            else:
                child = np.append(child, solution2[current : list_of_points[i]])

            current = list_of_points[i]

        if last_i % 2 == 0:
            child = np.append(child, solution2[list_of_points[-1] :])
        else:
            child = np.append(child, solution1[list_of_points[-1] :])

        return child
