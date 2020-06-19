from moead_framework.core.genetic_operator.combinatorial.crossover import Crossover
from moead_framework.core.genetic_operator.abstract_operator import GeneticOperator
from moead_framework.core.genetic_operator.combinatorial.mutation import BinaryMutation


class CrossoverAndMutation(GeneticOperator):

    def run(self):
        self.number_of_solution_is_correct(n=2)

        child = Crossover(solutions=self.solutions, crossover_points=self.crossover_points).run()
        child = BinaryMutation(solutions=[child]).run()

        return child
