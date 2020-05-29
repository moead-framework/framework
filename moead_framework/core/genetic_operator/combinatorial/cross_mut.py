from moead_framework.core.genetic_operator.combinatorial.crossover import Crossover
from moead_framework.core.genetic_operator.abstract_operator import GeneticOperator
from moead_framework.core.genetic_operator.combinatorial.mutation import BinaryMutation


class CrossoverAndMutation(GeneticOperator):

    def __init__(self, solution1, solution2, crossover_points=2):
        self.solution1 = solution1[:]
        self.solution2 = solution2[:]
        self.crossover_points = crossover_points

    def run(self):
        child = Crossover(self.solution1, self.solution2, self.crossover_points).run()
        child = BinaryMutation(child).run()

        return child
