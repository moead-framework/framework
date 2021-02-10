from abc import ABC, abstractmethod


class AggregationFunction(ABC):

    def __init__(self):
        pass

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

    @abstractmethod
    def is_better(self, old_value, new_value):
        """
        Allow to compare 2 aggregations values according to the aggregation function and to the context (minimization or maximization).

        :param old_value: {float}
        :param new_value: {float}
        :return: {boolean} True if new_value is better than old_value.
        The test depends of the aggregation function and of the context (minimization or maximization).
        """
