import numpy as np
from abc import ABC, abstractmethod

from moead_framework.solution.base import Solution


class AggregationFunction(ABC):
    """
    Abstract class to implement an aggregation function in the framework
    """

    @abstractmethod
    def run(self, solution, number_of_objective, weights, sub_problem, z):
        """
        Compute the aggregation value.

        :param solution: {:class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`}
        :param number_of_objective: {integer} number of objective
        :param weights: {list<list<integer>>} List of weight vectors
        :param sub_problem: {integer} index of the sub-problem / weight vector
        :param z: {list<float>} coordinates of the reference point Z*
        :return: {float} the aggregation value of the solution for the weight vector: weights[sub-problem]
        """
        if not isinstance(solution, Solution):
            raise TypeError(
                f"The parameter 'solution' of {self.__class__.__name__}.run() must be a child of the Solution class. Instead, we have {type(solution)}")

        if not isinstance(number_of_objective, int):
            raise TypeError(
                f"The parameter 'number_of_objective' of {self.__class__.__name__}.run() must be an integer. Instead, we have {type(number_of_objective)}")

        if not isinstance(weights, list):
            raise TypeError(
                f"The parameter 'weights' of {self.__class__.__name__}.run() must be a list. Instead, we have {type(weights)}")

        if not isinstance(sub_problem, int):
            raise TypeError(
                f"The parameter 'sub_problem' of {self.__class__.__name__}.run() must be an integer. Instead, we have {type(sub_problem)}")

        if (not isinstance(z, list)) & (not isinstance(z, np.ndarray)):
            raise TypeError(
                f"The parameter 'z' of {self.__class__.__name__}.run() must be a list. Instead, we have {type(z)}")
        else:
            if len(z) != number_of_objective:
                raise TypeError(
                    f"The number of items in the parameter 'z' of {self.__class__.__name__}.run() must be equals at {number_of_objective}. Instead, we have {len(z)}")

    @abstractmethod
    def is_better(self, old_value, new_value):
        """
        Allow to compare 2 aggregations values according to the aggregation function and to the context (minimization or maximization).

        :param old_value: {float}
        :param new_value: {float}
        :return: {boolean} True if new_value is better than old_value.
        The test depends of the aggregation function and of the context (minimization or maximization).
        """
        # if not isinstance(old_value, (np.floating, float)) & (not isinstance(new_value, (np.floating, float))):
        if ((not np.issubdtype(type(old_value), (np.floating))) & (not isinstance(old_value, int))) | (not np.issubdtype(type(new_value), (np.floating))) & (not isinstance(new_value, int)):
            raise TypeError(f"Parameters of {self.__class__.__name__}.is_better() must be float or int. Instead, we have {type(old_value)} and {type(new_value)}")
