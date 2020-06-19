from abc import ABC, abstractmethod


class GeneticOperator(ABC):

    def __init__(self, solutions, crossover_points=1):
        self.solutions = solutions
        self.crossover_points = crossover_points

    @abstractmethod
    def run(self):
        pass

    def number_of_solution_is_correct(self, n):
        if len(self.solutions) < n:
            raise ValueError("The genetic operator needs more than "+str(n)+" solutions")
