from abc import ABC, abstractmethod


class MatingPoolSelector(ABC):
    """
    select the set of solutions (the neighborhood) used to select parents
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
