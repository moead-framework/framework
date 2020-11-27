import random

from .moead import Moead
from moead_framework.core.selector.delta_selector import DeltaSelector
from moead_framework.tool.mop import is_duplicated, get_non_dominated


class MoeadDeltaNr(Moead):

    def __init__(self, problem,
                 max_evaluation,
                 number_of_objective,
                 number_of_weight,
                 number_of_weight_neighborhood,
                 delta,
                 number_of_replacement,
                 aggregation_function,
                 sps_strategy=None,
                 number_of_crossover_points=2,
                 parent_selector=None,
                 weight_file=None):

        mating_pool_selector = DeltaSelector
        self.delta = delta
        self.number_of_replacement = number_of_replacement
        self.mating_pool = []

        super().__init__(problem=problem,
                         max_evaluation=max_evaluation,
                         number_of_objective=number_of_objective,
                         number_of_weight=number_of_weight,
                         aggregation_function=aggregation_function,
                         number_of_weight_neighborhood=number_of_weight_neighborhood,
                         mating_pool_selector=mating_pool_selector,
                         parent_selector=parent_selector,
                         number_of_crossover_points=number_of_crossover_points,
                         sps_strategy=sps_strategy,
                         weight_file=weight_file)

    def update_solutions(self, solution, aggregation_function, sub_problem):
        """
        number_of_replacement is the maximal number of solutions replaced by each child solution
        to preserve the diversity.
        :param solution:
        :param aggregation_function:
        :param sub_problem:
        :return:
        """
        c = 0

        while (c < self.number_of_replacement) & (len(self.mating_pool) > 0):
            # Step (1)
            random_j = random.randint(0, len(self.mating_pool) - 1)
            j = self.mating_pool[random_j]

            j_score = aggregation_function.run(solution=self.population[j],
                                               number_of_objective=self.number_of_objective,
                                               weights=self.weights,
                                               sub_problem=j,
                                               z=self.z)

            y_score = aggregation_function.run(solution=solution,
                                               number_of_objective=self.number_of_objective,
                                               weights=self.weights,
                                               sub_problem=j,
                                               z=self.z)

            # Step (2)
            if aggregation_function.is_better(j_score, y_score):
                c += 1
                self.population[j] = solution
                if not is_duplicated(x=solution, population=self.ep, number_of_objective=self.number_of_objective):
                    self.ep.append(solution)
                    self.ep = get_non_dominated(self.ep)

            # Step (3)
            self.mating_pool.remove(j)
