from abc import ABC, abstractmethod


class GeneticOperator(ABC):

    def __init__(self, solutions, **kwargs):
        self.solutions = solutions

    @abstractmethod
    def run(self):
        pass

    def number_of_solution_is_correct(self, n):
        if len(self.solutions) < n:
            raise ValueError("The genetic operator needs more than "+str(n)+" solutions")
