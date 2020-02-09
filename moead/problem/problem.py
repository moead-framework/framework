from abc import abstractmethod, ABC


class Problem(ABC):

    @abstractmethod
    def __init__(self, objective_number=2):
        self.function_numbers = objective_number
        pass

    @abstractmethod
    def f(self, function_id, solution):
        pass

    @abstractmethod
    def generate_random_solution(self):
        pass

    @abstractmethod
    def generate_solution(self, array):
        pass