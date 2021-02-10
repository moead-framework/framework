from abc import ABC, abstractmethod


class ParentSelector(ABC):

    def __init__(self, algorithm):
        """
        :param algorithm: {:class:`~moead_framework.algorithm.abstract_moead.py.AbstractMoead`} instance of the algorithm
        """
        self.algorithm = algorithm

    @abstractmethod
    def select(self, indexes):
        """
        Select parents in the neighborhood represented by indexes

        :param indexes: {list<integer>} indexes of solutions used to select parents
        :return: {list<:class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`>} parents used to generate the future offspring
        """
