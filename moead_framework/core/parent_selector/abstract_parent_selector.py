from abc import ABC, abstractmethod

from moead_framework.algorithm import abstract_moead


class ParentSelector(ABC):
    """
    Abstract class to implement a new parent selector
    """

    def __init__(self, algorithm):
        """
        :param algorithm: {:class:`~moead_framework.algorithm.abstract_moead.py.AbstractMoead`} instance of the algorithm
        """

        if not isinstance(algorithm, abstract_moead.AbstractMoead):
            raise TypeError(f"The parameter 'algorithm' must be a child of the AbstractMoead class. Instead, we have {type(algorithm)}")
        self.algorithm = algorithm

    @abstractmethod
    def select(self, indexes):
        """
        Select parents in the neighborhood represented by indexes

        :param indexes: {list<integer>} indexes of solutions used to select parents
        :return: {list<:class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`>} parents used to generate the future offspring
        """
        if type(indexes) == list:
            if type(indexes[0]) == int:
                pass
            else:
                raise TypeError(
                    f"The type of parameter 'indexes' in {self.__class__.__name__}.select(indexes) must be a list<int>. Instead, we have list<{type(indexes)}>")
        else:
            raise TypeError(f"The type of parameter 'indexes' in {self.__class__.__name__}.select(indexes) must be a list<int>. Instead, we have {type(indexes)}")
