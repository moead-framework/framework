from abc import ABC, abstractmethod


class Function(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def run(self, solution, number_of_objective, weights, sub_problem, z):
        pass

    @abstractmethod
    def is_better(self, old_value, new_value):
        """
        :param old_value:
        :param new_value:
        :return: True if the new score return by run() is better than the old_value
        """
        pass
