from abc import ABC, abstractmethod


class MatingPoolSelector(ABC):

    def __init__(self, algorithm_instance):
        self.algorithm = algorithm_instance

    @abstractmethod
    def select(self, sub_problem):
        pass
