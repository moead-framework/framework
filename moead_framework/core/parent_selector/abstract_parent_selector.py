from abc import ABC, abstractmethod


class ParentSelector(ABC):

    def __init__(self, algorithm):
        self.algorithm = algorithm

    @abstractmethod
    def select(self, indexes):
        pass
