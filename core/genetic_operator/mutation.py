import random
from core.genetic_operator.abstract_operator import GeneticOperator


class Mutation(GeneticOperator):

    def __init__(self, solution):
        self.solution = solution[:]

    def run(self):
        n = len(self.solution)

        for i in range(len(self.solution)):
            probability = random.randint(0, n)

            if probability < (1 / n):
                self.solution[i] = abs(self.solution[i]-1)

        return self.solution