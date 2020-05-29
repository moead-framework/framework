import random

from .abstract_mating import OffspringGenerator


class OffspringGeneratorWithTwoRandomParents(OffspringGenerator):

    def run(self, population_indexes):

        index1 = population_indexes[random.randint(0, len(population_indexes) - 1)]
        index2 = population_indexes[random.randint(0, len(population_indexes) - 1)]

        parent1 = self.algorithm.population[index1]
        parent2 = self.algorithm.population[index2]

        y_sol = self.algorithm.genetic_operator(solution1=parent1.solution,
                                                solution2=parent2.solution,
                                                crossover_points=self.algorithm.number_of_crossover_points
                                                ).run()

        return self.algorithm.problem.generate_solution(array=y_sol)
