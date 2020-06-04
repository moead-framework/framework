import random
import numpy as np
from moead_framework.core.genetic_operator.abstract_operator import GeneticOperator
from moead_framework.core.genetic_operator.numerical.differential_evolution_crossover import \
    DifferentialEvolutionCrossover
from moead_framework.core.genetic_operator.numerical.polynomial_mutation import PolynomialMutation


class MoeadDeOperators(GeneticOperator):

    def __init__(self, solution1, solution2, solution3):
        self.solution1 = solution1[:]
        self.solution2 = solution2[:]
        self.solution3 = solution3[:]

    def run(self):
        child_cross = DifferentialEvolutionCrossover(self.solution1, self.solution2, self.solution3).run()
        child_mut = PolynomialMutation(child_cross)

        return child_mut



