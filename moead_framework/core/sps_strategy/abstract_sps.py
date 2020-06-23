from abc import ABC, abstractmethod


class SpsStrategy(ABC):

    def __init__(self, algorithm_instance):
        self.algorithm = algorithm_instance

    @abstractmethod
    def get_sub_problems(self):
        pass
