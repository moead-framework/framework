import random

import numpy as np

from moead_framework.core.offspring_generator.offspring_generator import OffspringGeneratorGeneric
from moead_framework.core.selector.closest_neighbors_selector import ClosestNeighborsSelector
from moead_framework.core.sps_strategy.sps_all import SpsAllSubproblems
from moead_framework.core.termination_criteria.max_evaluation import MaxEvaluation
from moead_framework.tool.mop import is_duplicated, get_non_dominated, generate_weight_vectors


class AbstractMoead:

    def __init__(self, problem, max_evaluation, number_of_weight_neighborhood,
                 aggregation_function, weight_file,
                 termination_criteria=None,
                 genetic_operator=None,
                 parent_selector=None,
                 mating_pool_selector=None,
                 sps_strategy=None,
                 offspring_generator=None,
                 number_of_weight=None,
                 number_of_objective=None,
                 ):
        """
        Constructor of the algorithm.

        :param problem: {:class:`~moead_framework.problem.Problem`} problem to optimize
        :param max_evaluation: {integer} maximum number of evaluation
        :param number_of_weight_neighborhood: {integer} size of the neighborhood.
        :param aggregation_function: {:class:`~moead_framework.aggregation.functions.AggregationFunction`}
        :param weight_file: {string} path of the weight file. Each line represent a weight vector, each column represent a coordinate. An exemple is available here: https://github.com/moead-framework/data/blob/master/weights/SOBOL-2objs-10wei.ws
        :param termination_criteria: Optional -- {:class:`~moead_framework.core.termination_criteria.abstract_termination_criteria.TerminationCriteria`} The default component is {:class:`~moead_framework.core.termination_criteria.max_evaluation.MaxEvaluation`}
        :param genetic_operator: Optional -- {:class:`~moead_framework.core.genetic_operator.abstract_operator.GeneticOperator`} The default operator depends of the problem type (combinatorial / numerical)
        :param parent_selector: Optional -- {:class:`~moead_framework.core.parent_selector.abstract_parent_selector.ParentSelector`} The default operator depends of the number of solution required by the genetic operator
        :param mating_pool_selector: Optional -- {:class:`~moead_framework.core.selector.abstract_selector.MatingPoolSelector`} The default selector is {:class:`~moead_framework.core.selector.closest_neighbors_selector.ClosestNeighborsSelector`}
        :param sps_strategy: Optional -- {:class:`~moead_framework.core.sps_strategy.abstract_sps.SpsStrategy`} The default strategy is {:class:`~moead_framework.core.sps_strategy.sps_all.SpsAllSubproblems`}
        :param offspring_generator: Optional -- {:class:`~moead_framework.core.offspring_generator.abstract_mating.OffspringGenerator`} The default generator is {:class:`~moead_framework.core.offspring_generator.offspring_generator.OffspringGeneratorGeneric`}
        :param number_of_weight: Deprecated -- {integer} number of weight vector used to decompose the problem. Deprecated, remove in the next major release.
        :param number_of_objective: Deprecated -- {integer} number of objective in the problem. Deprecated, remove in the next major release.
        """
        self.problem = problem
        self.aggregation_function = aggregation_function()

        if number_of_weight is not None:
            import warnings
            warnings.warn("The attribute number_of_weight is deprecated", DeprecationWarning)

        if number_of_objective is not None:
            import warnings
            warnings.warn("The attribute number_of_objective is deprecated", DeprecationWarning)

        if termination_criteria is None:
            self.termination_criteria = MaxEvaluation(algorithm_instance=self)
        else:
            self.termination_criteria = termination_criteria(algorithm_instance=self)

        self.max_evaluation = max_evaluation
        self.number_of_objective = self.problem.number_of_objective
        self.t = number_of_weight_neighborhood
        self.ep = []

        self.weights = generate_weight_vectors(weight_file, shuffle=False)
        self.number_of_weight = len(self.weights)
        self.population = self.initial_population()
        random.shuffle(self.weights)
        self.z = self.init_z()
        self.b = self.generate_closest_weight_vectors()
        self.current_sub_problem = -1
        self.current_eval = 1
        self.mating_pool = []

        if sps_strategy is None:
            self.sps_strategy = SpsAllSubproblems(algorithm_instance=self)
        else:
            self.sps_strategy = sps_strategy(algorithm_instance=self)

        if mating_pool_selector is None:
            self.mating_pool_selector = ClosestNeighborsSelector(algorithm_instance=self)
        else:
            self.mating_pool_selector = mating_pool_selector(algorithm_instance=self)

        self.genetic_operator = genetic_operator
        self.parent_selector = parent_selector

        if offspring_generator is None:
            self.offspring_generator = OffspringGeneratorGeneric(algorithm_instance=self)
        else:
            self.offspring_generator = offspring_generator(algorithm_instance=self)

    def run(self, checkpoint=None):
        """
        Execute the algorithm.

        :param checkpoint: {function} The default value is None. The checkpoint can be used to save data during the process
        :return:
        """
        while self.termination_criteria.test():

            # For each sub-problem i
            for i in self.get_sub_problems_to_visit():

                if checkpoint is not None:
                    checkpoint()

                self.update_current_sub_problem(sub_problem=i)
                self.mating_pool = self.mating_pool_selection(sub_problem=i)[:]
                y = self.generate_offspring(population=self.mating_pool)
                y = self.repair(solution=y)
                self.update_z(solution=y)
                self.update_solutions(solution=y, aggregation_function=self.aggregation_function, sub_problem=i)
                self.current_eval += 1

        return self.ep

    def update_solutions(self, solution, aggregation_function, sub_problem):
        """
        Update solutions of the population and of the external archive ep

        :param solution: {:class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`} the candidate solution also called offspring
        :param aggregation_function: {:class:`~moead_framework.aggregation.functions.AggregationFunction`} Aggregation function used to compare solution in a multi-objective context
        :param sub_problem: {integer} index of the sub-problem currently visited
        :return:
        """
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
                    self.ep = get_non_dominated(self.ep)

    def get_sub_problems_to_visit(self):
        """
        Select sub-problems to visit for the next generation.
        This function calls the component :class:`~moead_framework.core.sps_strategy.abstract_sps.SpsStrategy`

        :return: {list} indexes of sub-problems
        """
        return self.sps_strategy.get_sub_problems()

    def mating_pool_selection(self, sub_problem):
        """
        Select the set of solutions where future parents solutions will be selected according to the current sub-problem visited

        :param sub_problem: {integer} index of the sub-problem currently visited
        :return: {list} indexes of sub-problems
        """
        return self.mating_pool_selector.select(sub_problem)

    def generate_offspring(self, population):
        """
        Generate a new offspring.
        This function calls the component :class:`~moead_framework.core.offspring_generator.abstract_mating.py.OffspringGenerator`

        :param population: {list<:class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`>} set of solutions (parents) used to generate the offspring
        :return: {:class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`} offspring
        """
        return self.offspring_generator.run(population_indexes=population)

    def repair(self, solution):
        """
        Repair the solution in parameter.

        :param solution: {:class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`}
        :return: {:class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`} the repaired solution
        """
        return solution

    def update_current_sub_problem(self, sub_problem):
        """
        Update the attribute current_sub_problem

        :param sub_problem: {integer} index of sub-problem
        :return:
        """
        self.current_sub_problem = sub_problem

    def initial_population(self):
        """
        Initialize the population of solution

        :return: {List<:class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`>}
        """
        p = []
        for i in range(self.number_of_weight):
            x_i = self.problem.generate_random_solution()
            p.append(x_i)
            if not is_duplicated(x=x_i, population=self.ep, number_of_objective=self.number_of_objective):
                self.ep.append(x_i)
                self.ep = get_non_dominated(self.ep)

        return p

    def init_z(self):
        """
        Initialize the reference point z

        :return:
        """
        z = np.zeros(self.number_of_objective)

        for i in range(self.number_of_weight):
            for j in range(self.number_of_objective):
                f_j = self.population[i].F[j]

                if z[j] > f_j:  # in minimisation context !
                    z[j] = f_j

        return z

    def update_z(self, solution):
        """
        Update the reference point z with coordinates of the solution in parameter if coordinates are better.

        :param solution: :class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution` solution used to update the reference point
        :return:
        """
        for i in range(self.number_of_objective):
            if self.z[i] > solution.F[i]:  # in minimisation context !
                self.z[i] = solution.F[i]

    def generate_closest_weight_vectors(self):
        """
        Generate all neighborhood for each solution in the population

        :return: {list<List<Integer>>} List of sub-problem (neighborhood) for each solution
        """
        b = []
        for i in range(self.number_of_weight):
            b_i = np.zeros(self.t, int)
            b_dist = np.full(self.t, np.inf)
            for j in range(self.number_of_weight):
                dist_wi_wj = np.linalg.norm(np.array(self.weights[i]) - np.array(self.weights[j]))
                if dist_wi_wj < np.max(b_dist):
                    index_to_replace = np.argmax(b_dist)  # replace the worst distance
                    b_dist[index_to_replace] = dist_wi_wj
                    b_i[index_to_replace] = j

            b.append(b_i.tolist())

        return b
