from abc import ABC, abstractmethod


class SpsStrategy(ABC):

    def __init__(self, algorithm_instance):
        self.algorithm = algorithm_instance

    @abstractmethod
    def get_sub_problems(self):
        """
        get all sub-problems visited in the next generation
        :return: list of index that represents weight vectors
        """
