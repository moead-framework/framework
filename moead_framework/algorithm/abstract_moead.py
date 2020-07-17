import numpy as np
from abc import ABC, abstractmethod

from moead_framework.core.offspring_generator.offspring_generator import OffspringGeneratorGeneric
from moead_framework.core.selector.closest_neighbors_selector import ClosestNeighborsSelector
from moead_framework.core.sps_strategy.sps_all import SpsAllSubproblems
from moead_framework.core.termination_criteria.max_evaluation import MaxEvaluation
from moead_framework.tool.mop import is_duplicated, get_non_dominated, generate_weight_vectors


class AbstractMoead(ABC):

    def __init__(self, problem, max_evaluation, number_of_objective, number_of_weight, number_of_weight_neighborhood,
                 aggregation_function,
                 termination_criteria=None,
                 genetic_operator=None,
                 parent_selector=None,
                 mating_pool_selector=None,
                 sps_strategy=None,
                 offspring_generator=None,
                 weight_file=None):
        self.problem = problem
        self.aggregation_function = aggregation_function()

        if termination_criteria is None:
            self.termination_criteria = MaxEvaluation(algorithm_instance=self)
        else:
            self.termination_criteria = termination_criteria(algorithm_instance=self)

        self.max_evaluation = max_evaluation
        self.number_of_objective = number_of_objective
        self.number_of_weight = number_of_weight
        self.t = number_of_weight_neighborhood
        self.ep = []

        self.population = self.initial_population()
        self.weights = generate_weight_vectors(weight_file)
        self.z = self.init_z()
        self.b = self.generate_closest_weight_vectors()
        self.current_sub_problem = -1

        if sps_strategy is None:
            self.sps_strategy = SpsAllSubproblems(algorithm_instance=self)
        else:
            self.sps_strategy = sps_strategy(algorithm_instance=self)

        if mating_pool_selector is None:
            self.mating_pool_selector = ClosestNeighborsSelector(algorithm_instance=self)
        else:
            self.mating_pool_selector = mating_pool_selector

        self.genetic_operator = genetic_operator
        self.parent_selector = parent_selector

        if offspring_generator is None:
            self.offspring_generator = OffspringGeneratorGeneric(algorithm_instance=self)
        else:
            self.offspring_generator = offspring_generator(algorithm_instance=self)

    @abstractmethod
    def run(self, checkpoint=None):
        pass

    @abstractmethod
    def update_solutions(self, solution, scal_function, sub_problem):
        pass

    def get_sub_problems_to_visit(self):
        return self.sps_strategy.get_sub_problems()

    def mating_pool_selection(self, sub_problem):
        return self.mating_pool_selector.select(sub_problem)

    def generate_offspring(self, population):
        return self.offspring_generator.run(population_indexes=population)

    def repair(self, solution):
        return solution

    def update_current_sub_problem(self, sub_problem):
        self.current_sub_problem = sub_problem

    def initial_population(self):
        p = []
        for i in range(self.number_of_weight):
            x_i = self.problem.generate_random_solution()
            p.append(x_i)
            if not is_duplicated(x=x_i, population=self.ep, number_of_objective=self.number_of_objective):
                self.ep.append(x_i)
                self.ep = get_non_dominated(self.ep)

        return p

    def init_z(self):
        z = np.zeros(self.number_of_objective)

        for i in range(self.number_of_weight):
            for j in range(self.number_of_objective):
                f_j = self.population[i].F[j]

                if z[j] > f_j:  # in minimisation context !
                    z[j] = f_j

        return z

    def update_z(self, solution):
        for i in range(self.number_of_objective):
            if self.z[i] > solution.F[i]:  # in minimisation context !
                self.z[i] = solution.F[i]

    def generate_closest_weight_vectors(self):
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
