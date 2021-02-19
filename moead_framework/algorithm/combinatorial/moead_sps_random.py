from moead_framework.algorithm.combinatorial.moead import Moead
from moead_framework.core.sps_strategy.sps_random_and_boundaries import SpsRandomAndBoundaries


class MoeadSPSRandom(Moead):
    """
    Implementation of MOEA/D with the component :class:`~moead_framework.core.sps_strategy.sps_random_and_boundaries.SpsRandomAndBoundaries`.
    """

    def __init__(self, problem,
                 max_evaluation,
                 number_of_weight_neighborhood,
                 number_of_subproblem_to_visit,
                 aggregation_function,
                 weight_file,
                 number_of_objective=None,
                 number_of_crossover_points=None,
                 mating_pool_selector=None,
                 genetic_operator=None,
                 parent_selector=None,
                 ):
        """
        Constructor of the algorithm.

        :param problem: {:class:`~moead_framework.problem.Problem`} problem to optimize
        :param max_evaluation: {integer} maximum number of evaluation
        :param number_of_objective: {integer} number of objective in the problem
        :param number_of_weight_neighborhood: {integer} size of the neighborhood
        :param number_of_subproblem_to_visit: {integer} number of sub-problems to visit randomly at each generation
        :param weight_file: {string} path of the weight file. Each line represent a weight vector, each column represent a coordinate. An exemple is available here: https://github.com/moead-framework/data/blob/master/weights/SOBOL-2objs-10wei.ws
        :param aggregation_function: {:class:`~moead_framework.aggregation.functions.AggregationFunction`}
        :param genetic_operator: Optional -- {:class:`~moead_framework.core.genetic_operator.abstract_operator.GeneticOperator`} The default operator depends of the problem type (combinatorial / numerical)
        :param parent_selector: Optional -- {:class:`~moead_framework.core.parent_selector.abstract_parent_selector.ParentSelector`} The default operator depends of the number of solution required by the genetic operator
        :param mating_pool_selector: Optional -- {:class:`~moead_framework.core.selector.abstract_selector.MatingPoolSelector`} The default selector is {:class:`~moead_framework.core.selector.closest_neighbors_selector.ClosestNeighborsSelector`}
        :param number_of_objective: Deprecated -- {integer} number of objective in the problem. Deprecated, remove in the next major release.
        """

        super().__init__(problem=problem,
                         max_evaluation=max_evaluation,
                         number_of_objective=number_of_objective,
                         number_of_weight_neighborhood=number_of_weight_neighborhood,
                         aggregation_function=aggregation_function,
                         number_of_crossover_points=number_of_crossover_points,
                         genetic_operator=genetic_operator,
                         mating_pool_selector=mating_pool_selector,
                         parent_selector=parent_selector,
                         sps_strategy=SpsRandomAndBoundaries,
                         weight_file=weight_file)

        self.current_eval = 1
        self.number_of_subproblem = number_of_subproblem_to_visit
