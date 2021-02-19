from moead_framework.core.genetic_operator.combinatorial.crossover import Crossover
from moead_framework.core.genetic_operator.abstract_operator import GeneticOperator
from moead_framework.core.genetic_operator.combinatorial.mutation import BinaryMutation


class CrossoverAndMutation(GeneticOperator):
    """
    Multi-point crossover combined with the Binary Mutation operator

    Require 2 solutions, run a crossover according to the number of points wanted and
    try to mutate each bit of the solution with the predefined probability.
    """
    def __init__(self, solutions, **kwargs):
        """
        Constructor of the Crossover and Binary Mutation operator

        :param solutions: list<list<integer>> list of solution's representation (In algorithms, it is represented by the attribute :class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution.solution` of the class :class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`)
        :param crossover_points: {integer} the number of points for the crossover
        :param mutation_probability: {float} the probability (between 0 and 1) to mutate a bit in the solution. The default value is the probability to mutate one bit of the solution
        """
        super().__init__(solutions, **kwargs)
        if kwargs.get("crossover_points") is None:
            self.crossover_points = 1
        else:
            self.crossover_points = int(kwargs.get("crossover_points"))

        if kwargs.get("mutation_probability") is None:
            self.mutation_probability = 1 / (len(self.solutions[0]))
        else:
            self.mutation_probability = float(kwargs.get("mutation_probability"))

    def run(self):
        self.number_of_solution_is_correct(n=2)

        child = Crossover(solutions=self.solutions, crossover_points=self.crossover_points).run()
        child = BinaryMutation(solutions=[child], mutation_probability=self.mutation_probability).run()

        return child
