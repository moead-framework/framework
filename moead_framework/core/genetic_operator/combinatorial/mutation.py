import random
from moead_framework.core.genetic_operator.abstract_operator import GeneticOperator


class BinaryMutation(GeneticOperator):
    """
    Binary Mutation operator.

    Require only one solution. Try to mutate each bit of the solution with a predefined probability.
    """

    def __init__(self, solutions, **kwargs):
        """
        Constructor of the Binary Mutation operator

        :param solutions: list<list<integer>> list of solution's representation (In algorithms, it is represented by the attribute :class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution.solution` of the class :class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`)
        :param mutation_probability: {float} the probability to mutation a bit in the solution is 'mutation_probability / size(solution)'
        """
        super().__init__(solutions, **kwargs)
        if kwargs.get("mutation_probability") is None:
            self.mutation_probability = 1
        else:
            self.mutation_probability = int(kwargs.get("mutation_probability"))

    def run(self):

        self.number_of_solution_is_correct(n=1)

        solution = self.solutions[0]
        n = len(solution)

        for i in range(len(solution)):
            probability = random.randint(0, n)

            if probability < (self.mutation_probability / n):
                solution[i] = abs(solution[i]-1)

        return solution
