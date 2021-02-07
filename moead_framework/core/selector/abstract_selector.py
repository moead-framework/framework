from abc import ABC, abstractmethod


class MatingPoolSelector(ABC):

    def __init__(self, algorithm_instance):
        self.algorithm = algorithm_instance

    @abstractmethod
    def select(self, sub_problem):
        """
        select the set of solutions (the neighborhood) before to select parents
        :param sub_problem:
        :return: list of index that represents solutions in the population
        """
