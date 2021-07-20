from abc import ABC, abstractmethod


class SpsStrategy(ABC):
    """
    Abstract class to implement a new SPS Strategy
    """

    def __init__(self, algorithm_instance):
        """
        Constructor of the Sub-Problem Selection Strategy

        :param algorithm_instance: {:class:`~moead_framework.algorithm.abstract_moead.py.AbstractMoead`} instance of the algorithm
        """
        self.algorithm = algorithm_instance

    @abstractmethod
    def get_sub_problems(self):
        """
        Get all sub-problems visited in the next generation

        :return: {list<integer>} indexes of sub-problems
        """

    def get_xtrem_index(self):
        """
        get boundaries sub-problems

        :return: {list<integer>} indexes of sub-problems
        """
        xtrem_index = []
        for i in range(self.algorithm.number_of_weight):
            weight = self.algorithm.weights[i]
            for j in range(self.algorithm.number_of_objective):
                if weight[j] == 1:
                    xtrem_index.append(i)
                    break

        return xtrem_index
