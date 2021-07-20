from abc import ABC, abstractmethod


class GeneticOperator(ABC):
    """
    Abstract class to implement a new genetic Operator
    """

    def __init__(self, solutions, **kwargs):
        """
        Constructor of the genetic operator.

        :param solutions: list<list<integer>> list of solution's representation (In algorithms, it is represented by the attribute :class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution.decision_vector` of the class :class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`)
        :param kwargs: optional arguments for the genetic operator
        """
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
        if len(self.solutions) != n:
            msg = f"{self.__class__.__name__} needs {n} solutions as parents, but received {len(self.solutions)} solution(s)"
            raise ValueError(msg)
