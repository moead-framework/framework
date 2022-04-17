from abc import ABC, abstractmethod


class MatingPoolSelector(ABC):
    """
    Abstract class to implement a new mating-pool selector
    """

    def __init__(self, algorithm_instance):
        """
        Constructor of the mating pool selector

        :param algorithm_instance: {:class:`~moead_framework.algorithm.abstract_moead.py.AbstractMoead`} instance of the algorithm
        """
        self.algorithm = algorithm_instance

    @abstractmethod
    def select(self, sub_problem):
        """
        :param sub_problem: {integer} index of the current sub-problem visited
        :return: {list<integer>}
        """
        if type(sub_problem) != int:
            raise TypeError(
                f"The parameter 'select' of {self.__class__.__name__}.run() must be an integer. Instead, we have {type(sub_problem)}")

