import random
import numpy as np
from .abstract_operator import GeneticOperator


class DeCrossoverAndMut(GeneticOperator):

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

        return self.mutation1(s=child, rate=1/len(self.solution1), n=len(self.solution1))

    def repair(self, s, mini=0, maxi=1):
        return [mini if x < mini else maxi if x > maxi else x for x in s]

    def mutation1(self, s, rate, n=20, mini=0, maxi=1):
        rand = random.uniform(0, 1)
        return self.repair([s[x] if rand > rate else s[x] + self.sigma(n) * (maxi - (mini)) for x in range(len(s))])

    def sigma(self, n):
        rand = random.uniform(0, 1)
        sigma = 0
        if rand < 0.5:
            sigma = pow(2 * rand, 1 / (n + 1)) - 1
        else:
            sigma = 1 - pow(2 - 2 * rand, 1 / (n - 1))
        return sigma
