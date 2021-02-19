import random
import numpy as np
from moead_framework.algorithm.combinatorial.moead_delta_nr import MoeadDeltaNr
from moead_framework.core.sps_strategy.sps_dra import SpsDra


class MoeadDRA(MoeadDeltaNr):
    """
    Implementation of MOEA/D-DRA

    Q. Zhang, W. Liu, and H. Li. The performance of a new version of moea/d on cec09 unconstrained mop test instances. In 2009 IEEE Congress on Evolutionary Computation, volume, 203–208. 2009. doi:10.1109/CEC.2009.4982949.
    """

    def __init__(self, problem,
                 max_evaluation,
                 number_of_weight_neighborhood,
                 delta,
                 number_of_replacement,
                 aggregation_function,
                 weight_file,
                 number_of_objective=None,
                 number_of_crossover_points=None,
                 threshold_before_evaluate_subproblem_utility=50,
                 delta_threshold=0.001,
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
        :param number_of_crossover_points: {integer} number of crossover point
        :param threshold_before_evaluate_subproblem_utility: Optional -- Threshold before evaluate the subproblem utility. The default value is 50
        :param delta_threshold: Optional -- reset the utility if the relative decrease delta_i is under this treshold. The default value is 0.001
        :param number_of_objective: Deprecated -- {integer} number of objective in the problem. Deprecated, remove in the next major release.
        """

        super().__init__(problem=problem,
                         max_evaluation=max_evaluation,
                         number_of_objective=number_of_objective,
                         number_of_weight_neighborhood=number_of_weight_neighborhood,
                         delta=delta,
                         number_of_replacement=number_of_replacement,
                         aggregation_function=aggregation_function,
                         number_of_crossover_points=number_of_crossover_points,
                         sps_strategy=SpsDra,
                         weight_file=weight_file)

        self.pi = np.ones(self.number_of_weight)
        self.gen = 0
        self.current_eval = 1
        self.threshold_before_evaluate_subproblem_utility = threshold_before_evaluate_subproblem_utility
        self.delta_threshold = delta_threshold
        self.mating_pool = []
        self.scores = []
        for i in range(self.number_of_weight):
            self.scores.append([0, 0])

    def run(self, checkpoint=None):

        while self.current_eval < self.max_evaluation:

            for i in self.get_sub_problems_to_visit():

                if checkpoint is not None:
                    checkpoint(self.current_eval)

                self.update_current_sub_problem(sub_problem=i)
                self.mating_pool = self.mating_pool_selection(sub_problem=i)[:]
                y = self.generate_offspring(population=self.mating_pool)
                y = self.repair(solution=y)
                self.update_z(solution=y)
                self.update_solutions(solution=y, aggregation_function=self.aggregation_function, sub_problem=i)
                self.current_eval += 1

            # update the score history of all sub_problem
            # just before compute the utility of sub problems

            if ((self.gen + 1) % self.threshold_before_evaluate_subproblem_utility == 0) | (self.gen == 0):
                all_sub_problems = list(range(self.number_of_weight))
                for i in all_sub_problems:
                    score = self.aggregation_function.run(solution=self.population[i],
                                                          number_of_objective=self.number_of_objective,
                                                          weights=self.weights,
                                                          sub_problem=i,
                                                          z=self.z)
                    self.update_scores(sub_problem=i, score=score)

            self.gen += 1
            if self.gen % self.threshold_before_evaluate_subproblem_utility == 0:
                self.update_pi()

        return self.ep

    def update_scores(self, sub_problem, score):
        """
        Update the score

        self.scores[sub_problem][0] = old score
        self.scores[sub_problem][1] = new score

        :param sub_problem: {integer} index of the current sub-problem
        :param score: {float}
        :return:
        """
        self.scores[sub_problem][0] = self.scores[sub_problem][1]
        self.scores[sub_problem][1] = score

    def compute_delta(self, i):
        """
        compute the relative decrease delta_i

        :param i: {integer} index of sub-problem
        :return:
        """
        old_value = self.scores[i][0]
        new_value = self.scores[i][1]

        if old_value == 0:
            old_value = new_value
            if new_value == 0:
                return 0  # when g return 0
        return (old_value - new_value) / old_value

    def update_pi(self):
        """
        update the utility of each sub_problem

        :return:
        """
        # for each sub_problem
        for i in range(self.number_of_weight):
            if self.gen % 50 == 0:
                delta_i = self.compute_delta(i=i)

                if delta_i > self.delta_threshold:
                    self.pi[i] = 1
                else:
                    old_pi = self.pi[i]
                    self.pi[i] = (0.95 + 0.05 * (delta_i / self.delta_threshold)) * old_pi
