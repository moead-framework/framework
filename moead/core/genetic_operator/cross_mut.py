from .crossover import Crossover
from .abstract_operator import GeneticOperator
from .mutation import Mutation


class CrossoverAndMutation(GeneticOperator):

    def __init__(self, solution1, solution2, crossover_points=2):
        self.solution1 = solution1[:]
        self.solution2 = solution2[:]
        self.crossover_points = crossover_points

    def run(self):
        child = Crossover(self.solution1, self.solution2, self.crossover_points).run()
        child = Mutation(child).run()

        return child
