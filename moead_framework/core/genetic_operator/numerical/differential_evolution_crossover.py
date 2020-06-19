import random
from moead_framework.core.genetic_operator.abstract_operator import GeneticOperator


class DifferentialEvolutionCrossover(GeneticOperator):

    def run(self):
        self.number_of_solution_is_correct(n=3)
        solution1 = self.solutions[0]
        solution2 = self.solutions[1]
        solution3 = self.solutions[2]

        CR = 1.0
        F = 0.5

        s = []

        # Crossover
        for x in range(len(solution1)):
            if random.uniform(0, 1) < CR:
                s = s + [(solution1[x] + F * (solution2[x] - solution3[x]))]
            else:
                s = s + [solution1[x]]

        child = self.repair(s)

        return child

    def repair(self, s, mini=0, maxi=1):
        return [mini if x < mini else maxi if x > maxi else x for x in s]

