from moead_framework.core.genetic_operator.combinatorial.crossover import Crossover
from moead_framework.core.genetic_operator.abstract_operator import GeneticOperator
from moead_framework.core.genetic_operator.combinatorial.mutation import BinaryMutation


class CrossoverAndMutation(GeneticOperator):
    """
    Multi-point crossover combined with the Binary Mutation operator

    Require 2 solutions, run a crossover according to the number of points crossover_points and
    try to mutate each bit of the solution with the probability mutation_probability.
    """
    def __init__(self, solutions, **kwargs):
        super().__init__(solutions, **kwargs)
        if kwargs.get("crossover_points") is None:
            self.crossover_points = 1
        else:
            self.crossover_points = int(kwargs.get("crossover_points"))

        if kwargs.get("mutation_probability") is None:
            self.mutation_probability = 1
        else:
            self.mutation_probability = int(kwargs.get("mutation_probability"))

    def run(self):
        self.number_of_solution_is_correct(n=2)

        child = Crossover(solutions=self.solutions, crossover_points=self.crossover_points).run()
        child = BinaryMutation(solutions=[child], mutation_probability=self.mutation_probability).run()

        return child
