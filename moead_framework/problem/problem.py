from abc import abstractmethod, ABC
from typing import Union, Sequence

import numpy as np
from moead_framework.solution.base import Solution
from moead_framework.solution import OneDimensionSolution


class Problem(ABC):
    """
     Abstract class to implement a new Problem in the framework.

     https://moead-framework.github.io/framework/html/tuto.html#implement-your-own-problem
    """

    dtype = float

    def __init__(self, objective_number=2):
        """
        Constructor of the problem

        :param objective_number: {integer}
        """
        self.number_of_objective = objective_number
        pass

    @abstractmethod
    def f(self, function_id, decision_vector):
        """
        Evaluate the decision_vector for the objective function_id

        :param function_id: {integer} index of the objective
        :param decision_vector: {:class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`} solution to evaluate
        :return: {float} fitness value
        """


    @abstractmethod
    def generate_random_solution(self):
        """
        Generate a random solution for the current problem

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
        x.F = [self.f(j, x.decision_vector) for j in range(self.number_of_objective)]
        return x
