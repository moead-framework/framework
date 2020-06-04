import random
from moead_framework.core.genetic_operator.abstract_operator import GeneticOperator


class DifferentialEvolutionCrossover(GeneticOperator):

    def __init__(self, solution1, solution2, solution3):
        self.solution1 = solution1[:]
        self.solution2 = solution2[:]
        self.solution3 = solution3[:]

    def run(self):
        CR = 1.0
        F = 0.5

        s = []

        # Crossover
        for x in range(len(self.solution1)):
            if random.uniform(0, 1) < CR:
                s = s + [(self.solution1[x] + F * (self.solution2[x] - self.solution3[x]))]
            else:
                s = s + [self.solution1[x]]

        child = self.repair(s)

        return child

    def repair(self, s, mini=0, maxi=1):
        return [mini if x < mini else maxi if x > maxi else x for x in s]

