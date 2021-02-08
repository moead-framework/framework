from abc import abstractmethod, ABC


class Problem(ABC):

    def __init__(self, objective_number=2):
        self.function_numbers = objective_number
        pass

    @abstractmethod
    def f(self, function_id, solution):
        """
        Evaluate the solution for the objective function_id

        :param function_id: {integer} index of the objective
        :param solution: {:class:`~moead_framework.solution.one_dimension_solution`} solution to evaluate
        :return: {float} fitness value
        """


    @abstractmethod
    def generate_random_solution(self, evaluate=True):
        """
        Generate a random Solution for the current problem

        :param evaluate: Boolean: specify if the new solution is evaluated. The default value is True.
        :return: {:class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`}
        """

    @abstractmethod
    def generate_solution(self, array, evaluate=True):
        """
        Generate a predefined Solution for the current problem with array

        :param array: List: all decision variables of the Solution
        :param evaluate: Boolean: specify if the new solution is evaluated. The default value is True.
        :return: {:class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`}
        """
