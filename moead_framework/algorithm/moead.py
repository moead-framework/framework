from .abstract_moead import AbstractMoead
from ..tool.mop import get_non_dominated, is_duplicated


class Moead(AbstractMoead):

    def __init__(self, problem,
                 max_evaluation,
                 number_of_objective,
                 number_of_weight,
                 number_of_weight_neighborhood,
                 number_of_crossover_points=2,
                 mating_pool_selector=None,
                 genetic_operator=None,
                 mating=None,
                 weight_file=None):

        self.current_eval = 1
        self.mating_pool = []

        super().__init__(problem,
                         max_evaluation,
                         number_of_objective,
                         number_of_weight,
                         number_of_weight_neighborhood,
                         number_of_crossover_points,
                         genetic_operator=genetic_operator,
                         mating_pool_selector=mating_pool_selector,
                         mating=mating,
                         weight_file=weight_file)

    def run(self, g, checkpoint=None):

        while self.current_eval < self.max_evaluation:

            # For each sub-problem i
            for i in self.sps_strategy():

                if checkpoint is not None:
                    checkpoint()

                self.update_current_sub_problem(sub_problem=i)
                self.mating_pool = self.mating_pool_selection(sub_problem=i)[:]
                y = self.reproduction(population=self.mating_pool)
                y = self.repair(solution=y)
                self.update_z(solution=y)
                self.update_solutions(solution=y, aggregation_function=g, sub_problem=i)
                self.current_eval += 1

        return self.ep

    def sps_strategy(self):
        return range(self.number_of_weight)

    def mating_pool_selection(self, sub_problem):
        return self.mating_pool_selector.select(sub_problem)

    def reproduction(self, population):
        return self.mating(algorithm_instance=self).run(population_indexes=population)

    def repair(self, solution):
        return solution

    def update_solutions(self, solution, aggregation_function, sub_problem):

        for j in self.b[sub_problem]:
            y_score = aggregation_function.run(solution=solution,
                                               number_of_objective=self.number_of_objective,
                                               weights=self.weights,
                                               sub_problem=j,
                                               z=self.z)

            pop_j_score = aggregation_function.run(solution=self.population[j],
                                                   number_of_objective=self.number_of_objective,
                                                   weights=self.weights,
                                                   sub_problem=j,
                                                   z=self.z)

            if aggregation_function.is_better(pop_j_score, y_score):
                self.population[j] = solution

                if not is_duplicated(x=solution, population=self.ep, number_of_objective=self.number_of_objective):
                    self.ep.append(solution)
                    self.ep = get_non_dominated(self.ep, self.number_of_objective)

