from abc import ABC, abstractmethod


class GeneticOperator(ABC):

    @abstractmethod
    def run(self):
        pass
