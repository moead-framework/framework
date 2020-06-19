from abc import ABC, abstractmethod


class AggregationFunction(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def run(self, solution, number_of_objective, weights, sub_problem, z):
        """
        :param solution:
        :param number_of_objective:
        :param weights:
        :param sub_problem:
        :param z:
        :return: the aggregation value of the solution for the weight weights[sub-problem]
        """
        pass

    @abstractmethod
    def is_better(self, old_value, new_value):
        """
        :param old_value:
        :param new_value:
        :return: True if new_value (computed by run()) is better than old_value.
        The test depends of the aggregation function and of the context (minimization or maximization).
        """
        pass
