from abc import ABC, abstractmethod


class OffspringGenerator(ABC):
    """
    Generate a new offspring.
    """

    def __init__(self, algorithm_instance):
        self.algorithm = algorithm_instance

    @abstractmethod
    def run(self, population_indexes):
        """
        Execute the process to generate a new candidate solution

        :param population_indexes: {list<integer>} indexes of parents in the population used to generate the offspring
        :return: {:class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`} offspring
        """
