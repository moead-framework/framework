import numpy as np
from abc import ABC, abstractmethod

from ..tool.mop import is_duplicated, get_non_dominated, generate_weight_vectors


class AbstractMoead(ABC):

    def __init__(self, problem, max_evaluation, number_of_objective, number_of_weight, number_of_weight_neighborhood,
                 number_of_crossover_points=2,
                 genetic_operator=None,
                 offspring_generator=None,
                 mating_pool_selector=None,
                 weight_file=None):
        self.problem = problem
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

        self.mating_pool_selector = mating_pool_selector
        self.genetic_operator = genetic_operator
        self.offspring_generator = offspring_generator

    @abstractmethod
    def run(self, scalarizing_function, checkpoint=None):
        pass

    @abstractmethod
    def sps_strategy(self):
        pass

    @abstractmethod
    def mating_pool_selection(self, sub_problem):
        pass

    @abstractmethod
    def generate_offspring(self, population):
        pass

    @abstractmethod
    def repair(self, solution):
        pass

    @abstractmethod
    def update_solutions(self, solution, scal_function, sub_problem):
        pass

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
