from abc import abstractmethod, ABC


class Problem(ABC):

    def __init__(self, objective_number=2):
        self.function_numbers = objective_number
        pass

    @abstractmethod
    def f(self, function_id, solution):
        """
        Evaluate the solution for the objective function_id
        :param function_id: index of the objective
        :param solution: Solution to evaluate
        :return: (float) fitness value
        """


    @abstractmethod
    def generate_random_solution(self, evaluate=True):
        """
        Generate a random Solution for the current problem
        :param evaluate: Boolean to specify if the new solution is evaluated
        :return: Solution
        """

    @abstractmethod
    def generate_solution(self, array, evaluate=True):
        """
        Generate a predefined Solution for the current problem with array
        :param array: List with all decision variables of the Solution
        :param evaluate: Boolean to specify if the new solution is evaluated
        :return: Solution
        """
