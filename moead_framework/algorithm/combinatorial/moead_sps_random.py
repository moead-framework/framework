import random
from moead_framework.algorithm.combinatorial.moead import Moead
from moead_framework.core.sps_strategy.sps_random_and_boundaries import SpsRandomAndBoundaries


class MoeadSPSRandom(Moead):

    def __init__(self, problem,
                 max_evaluation,
                 number_of_objective,
                 number_of_weight,
                 number_of_weight_neighborhood,
                 number_of_subproblem_to_visit,
                 aggregation_function,
                 number_of_crossover_points=2,
                 mating_pool_selector=None,
                 genetic_operator=None,
                 parent_selector=None,
                 weight_file=None
                 ):

        super().__init__(problem,
                         max_evaluation,
                         number_of_objective,
                         number_of_weight,
                         number_of_weight_neighborhood,
                         aggregation_function=aggregation_function,
                         number_of_crossover_points=number_of_crossover_points,
                         genetic_operator=genetic_operator,
                         mating_pool_selector=mating_pool_selector,
                         parent_selector=parent_selector,
                         sps_strategy=SpsRandomAndBoundaries,
                         weight_file=weight_file)

        self.current_eval = 1
        self.number_of_subproblem = number_of_subproblem_to_visit
