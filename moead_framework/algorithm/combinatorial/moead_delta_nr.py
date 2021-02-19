import random

from .moead import Moead
from moead_framework.core.selector.delta_selector import DeltaSelector
from moead_framework.tool.mop import is_duplicated, get_non_dominated


class MoeadDeltaNr(Moead):
    """
    Implementation of MOEA/D with parameters delta / nr

    H. Li and Q. Zhang. MOEA/D-DE : Multiobjective Optimization Problems With Complicated Pareto Sets, MOEA/D and NSGA-II. IEEE Transactions on Evolutionary Computation, 13(2):284–302, April 2009. doi:10.1109/TEVC.2008.925798
    """

    def __init__(self, problem,
                 max_evaluation,
                 number_of_objective,
                 number_of_weight_neighborhood,
                 delta,
                 number_of_replacement,
                 aggregation_function,
                 weight_file,
                 sps_strategy=None,
                 number_of_crossover_points=None,
                 mutation_probability=None,
                 parent_selector=None,
                 ):
        """
        Constructor of the algorithm.

        :param problem: {:class:`~moead_framework.problem.Problem`} problem to optimize
        :param max_evaluation: {integer} maximum number of evaluation
        :param number_of_weight_neighborhood: {integer} size of the neighborhood
        :param delta: {float} probability to use all the population as neighborhood
        :param number_of_replacement: {integer} maximum number of solutions replaced in the population for each new offspring generated
        :param aggregation_function: {:class:`~moead_framework.aggregation.functions.AggregationFunction`}
        :param weight_file: {string} path of the weight file. Each line represent a weight vector, each column represent a coordinate. An exemple is available here: https://github.com/moead-framework/data/blob/master/weights/SOBOL-2objs-10wei.ws
        :param parent_selector: Optional -- {:class:`~moead_framework.core.parent_selector.abstract_parent_selector.ParentSelector`} The default operator depends of the number of solution required by the genetic operator
        :param sps_strategy: Optional -- {:class:`~moead_framework.core.sps_strategy.abstract_sps.SpsStrategy`} The default strategy is {:class:`~moead_framework.core.sps_strategy.sps_all.SpsAllSubproblems`}
        :param number_of_crossover_points: {integer} number of crossover point
        :param mutation_probability: {integer} probability of mutation used by the genetic operator
        :param number_of_objective: Deprecated -- {integer} number of objective in the problem. Deprecated, remove in the next major release.
        """

        mating_pool_selector = DeltaSelector
        self.delta = delta
        self.number_of_replacement = number_of_replacement
        self.mating_pool = []

        super().__init__(problem=problem,
                         max_evaluation=max_evaluation,
                         number_of_objective=number_of_objective,
                         aggregation_function=aggregation_function,
                         number_of_weight_neighborhood=number_of_weight_neighborhood,
                         mating_pool_selector=mating_pool_selector,
                         parent_selector=parent_selector,
                         number_of_crossover_points=number_of_crossover_points,
                         mutation_probability=mutation_probability,
                         sps_strategy=sps_strategy,
                         weight_file=weight_file)

    def update_solutions(self, solution, aggregation_function, sub_problem):
        """
        Update solutions of the population and of the external archive ep.

        Integration of the parameter number_of_replacement (the maximal number of solutions replaced by each child solution
        to preserve the diversity)

        :param solution: {:class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`} the candidate solution also called offspring
        :param aggregation_function: {:class:`~moead_framework.aggregation.functions.AggregationFunction`} Aggregation function used to compare solution in a multi-objective context
        :param sub_problem: {integer} index of the sub-problem currently visited
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
