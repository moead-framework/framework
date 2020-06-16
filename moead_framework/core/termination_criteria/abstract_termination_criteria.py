from abc import ABC, abstractmethod


class TerminationCriteria(ABC):

    def __init__(self, algorithm_instance):
        self.algorithm = algorithm_instance

    @abstractmethod
    def test(self):
        pass
