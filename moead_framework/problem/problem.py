from abc import abstractmethod, ABC
from typing import Union, Sequence

import numpy as np
from moead_framework.solution.solution import Solution
from moead_framework.solution import OneDimensionSolution


class Problem(ABC):

    dtype = float

    def __init__(self, objective_number=2):
        self.number_of_objective = objective_number
        pass

    @abstractmethod
    def f(self, function_id, solution):
        """
        Evaluate the solution for the objective function_id

        :param function_id: {integer} index of the objective
        :param solution: {:class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`} solution to evaluate
        :return: {float} fitness value
        """


    @abstractmethod
    def generate_random_solution(self, evaluate=True):
        """
        Generate a random solution for the current problem

        :param evaluate: {boolean} specify if the new solution is evaluated. The default value is True.
        :return: {:class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`}
        """

    def evaluate(self, x: Union[Solution, Sequence]) -> OneDimensionSolution:
        """
        Evaluate the given solution for the current problem and store the outcome

        :param x: A {Solution} containing all decision variables
        :return: :class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`
        """
        if not isinstance(x, OneDimensionSolution):
            x = OneDimensionSolution(np.array(x, dtype=self.dtype))
        x.F = [self.f(j, x.solution) for j in range(self.number_of_objective)]
        return x
