import random

from .abstract_mating import OffspringGenerator


class OffspringGeneratorGeneric(OffspringGenerator):
    """
    Generate a new offspring by using 2 components: the parent selector and the genetic operator
    """

    def run(self, population_indexes):

        parents = self.algorithm.parent_selector.select(indexes=population_indexes)

        parents_solutions = []
        for s in parents:
            parents_solutions.append(s.solution)

        if hasattr(self.algorithm, 'number_of_crossover_points'):
            crossover_point = self.algorithm.number_of_crossover_points
        else:
            crossover_point = None

        if hasattr(self.algorithm, 'mutation_probability'):
            mutation_probability = self.algorithm.mutation_probability
        else:
            mutation_probability = None

        y_sol = self.algorithm.genetic_operator(solutions=parents_solutions,
                                                crossover_points=crossover_point,
                                                mutation_probability=mutation_probability
                                                ).run()

        return self.algorithm.problem.generate_solution(array=y_sol)
