from abc import ABC, abstractmethod


class ParentSelector(ABC):

    def __init__(self, algorithm):
        self.algorithm = algorithm

    @abstractmethod
    def select(self, indexes):
        """
        Select parents in the neighborhood represented by indexes
        :param indexes: list of index of solutions in the population
        :return: a list of Solution object
        """
