import random
import numpy as np
from moead_framework.core.genetic_operator.abstract_operator import GeneticOperator
from moead_framework.core.genetic_operator.numerical.differential_evolution_crossover import \
    DifferentialEvolutionCrossover
from moead_framework.core.genetic_operator.numerical.polynomial_mutation import PolynomialMutation


class MoeadDeOperators(GeneticOperator):

    def run(self):
        self.number_of_solution_is_correct(n=3)
        solution1 = self.solutions[0]
        solution2 = self.solutions[1]
        solution3 = self.solutions[2]

        child_cross = DifferentialEvolutionCrossover(solutions=[solution1.solution,
                                                                solution2.solution,
                                                                solution3.solution]).run()
        child_mut = PolynomialMutation(solution=[child_cross])

        return child_mut



