from abc import ABC, abstractmethod


class OffspringGenerator(ABC):

    def __init__(self, algorithm_instance):
        self.algorithm = algorithm_instance

    @abstractmethod
    def run(self, population_indexes):
        """
        Execute the process to generate a new candidate solution
        :param population_indexes: index vector of parents in the population used to generate the offspring
        :return: Solution
        """
