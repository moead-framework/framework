import random
import numpy as np
from moead_framework.core.genetic_operator.abstract_operator import GeneticOperator


class PolynomialMutation(GeneticOperator):

    def run(self):
        self.number_of_solution_is_correct(n=1)
        solution = self.solutions[0]

        return self.mutation(s=solution, rate=1/len(solution), n=len(solution))

    def repair(self, s, mini=0, maxi=1):
        return [mini if x < mini else maxi if x > maxi else x for x in s]

    def mutation(self, s, rate, n=20, mini=0, maxi=1):
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
