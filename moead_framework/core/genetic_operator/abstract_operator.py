import numpy as np
from abc import ABC, abstractmethod


class GeneticOperator(ABC):
    """
    Abstract class to implement a new genetic Operator
    """

    def __init__(
        self,
        solutions,
    ):
        """
        Constructor of the genetic operator.

        :param solutions: list<list<integer>> list of solution's representation (In algorithms, it is represented by the attribute :class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution.decision_vector` of the class :class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`)
        """
        if type(solutions) == list:
            if (type(solutions[0]) == list) | (type(solutions[0]) == np.ndarray):
                pass
            else:
                raise AttributeError(f"The type of parameter 'solutions' must be list<list<Int>>, received list<{type(solutions[0])}>")
        else:
            raise AttributeError(f"The type of parameter 'solutions' must be list<list<Int>>, received {type(solutions)}>")

        if len(solutions) == 0:
            raise AttributeError(f"The parameter solutions of {self.__class__.__name__} can't be empty.")

        for solution in solutions:
            if len(solution) == 0:
                raise AttributeError(f"One of solutions in the parameter 'solutions' of {self.__class__.__name__} is empty.")

            for variable in solution:
                if type(variable) == str:
                    raise AttributeError(f"One of variable in {solution} is not a int or float, received {type(variable)} ({variable})")
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
