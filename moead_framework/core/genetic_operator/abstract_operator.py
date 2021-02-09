from abc import ABC, abstractmethod


class GeneticOperator(ABC):

    def __init__(self, solutions, **kwargs):
        self.solutions = solutions

    @abstractmethod
    def run(self):
        """
        Execute the genetic operator

        :return: {:class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`} the offspring
        """

    def number_of_solution_is_correct(self, n):
        """
        Secure the number of solutions required by the operator.
        it allows to check if the operator has the required number of solutions for the process in run()

        :param n: {integer} number of solution required by the operator
        :return:
        """
        if len(self.solutions) < n:
            raise ValueError("The genetic operator needs more than "+str(n)+" solutions")
