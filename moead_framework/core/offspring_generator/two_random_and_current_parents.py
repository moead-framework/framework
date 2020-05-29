import random

from .abstract_mating import OffspringGenerator


class OffspringGeneratorWithTwoRandomAndCurrentParents(OffspringGenerator):

    def run(self, population_indexes):
        index2 = population_indexes[random.randint(0, len(population_indexes) - 1)]
        index3 = population_indexes[random.randint(0, len(population_indexes) - 1)]

        parent1 = self.algorithm.population[self.algorithm.current_sub_problem]
        parent2 = self.algorithm.population[index2]
        parent3 = self.algorithm.population[index3]

        y_sol = self.algorithm.genetic_operator(solution1=parent1.solution,
                                                solution2=parent2.solution,
                                                solution3=parent3.solution
                                                ).run()

        return self.algorithm.problem.generate_solution(array=y_sol)
