import random

from .abstract_mating import OffspringGenerator


class OffspringGeneratorGeneric(OffspringGenerator):
    """
    Generate a new offspring by using 2 components: the parent selector and the genetic operator
    """

    def run(self, population_indexes):
        """
        Execute the process to generate a new candidate solution

        :param population_indexes: {list<integer>} indexes of parents in the population used to generate the offspring
        :return: {:class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`} offspring
        """

        parents = self.algorithm.parent_selector.select(indexes=population_indexes)

        parents_solutions = []
        for s in parents:
            parents_solutions.append(s.decision_vector)

        params = {"solutions": parents_solutions}
        proba = 'mutation_probability'
        
        if hasattr(self.algorithm, "number_of_crossover_points"):
            params["crossover_points"] = self.algorithm.number_of_crossover_points

        if hasattr(self.algorithm, proba):
            params[proba] = self.algorithm.mutation_probability

        y_sol = self.algorithm.genetic_operator(**params).run()

        return self.algorithm.problem.evaluate(x=y_sol)
