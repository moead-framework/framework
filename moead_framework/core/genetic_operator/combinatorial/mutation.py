import random
from moead_framework.core.genetic_operator.abstract_operator import GeneticOperator


class BinaryMutation(GeneticOperator):

    def run(self):

        self.number_of_solution_is_correct(n=1)

        solution = self.solutions[0]
        n = len(solution)

        for i in range(len(solution)):
            probability = random.randint(0, n)

            if probability < (1 / n):
                solution[i] = abs(solution[i]-1)

        return solution
