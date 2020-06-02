import random
from moead_framework.algorithm.combinatorial.moead import Moead


class MoeadSPSRandom(Moead):

    def __init__(self, problem,
                 max_evaluation,
                 number_of_objective,
                 number_of_weight,
                 number_of_weight_neighborhood,
                 number_of_subproblem,
                 number_of_crossover_points=2,
                 mating_pool_selector=None,
                 genetic_operator=None,
                 offspring_generator=None,
                 weight_file=None
                 ):

        super().__init__(problem,
                         max_evaluation,
                         number_of_objective,
                         number_of_weight,
                         number_of_weight_neighborhood,
                         number_of_crossover_points,
                         genetic_operator=genetic_operator,
                         mating_pool_selector=mating_pool_selector,
                         offspring_generator=offspring_generator,
                         weight_file=weight_file)

        self.current_eval = 1
        self.number_of_subproblem = number_of_subproblem

    def sps_strategy(self):
        """
        Select one random sub problems in each cluster
        :return: an array of sub problems
        """
        range_list = list(range(self.number_of_weight))
        xtrem_index = self.get_xtrem_index()
        random_indexes = random.sample(list(set(range_list)-set(xtrem_index)), self.number_of_subproblem)

        random_indexes = random_indexes + xtrem_index
        random.shuffle(random_indexes)

        return random_indexes

    def get_xtrem_index(self):
        xtrem_index = []
        for i in range(self.number_of_weight):
            weight = self.weights[i]
            for j in range(self.number_of_objective):
                if weight[j] == 1:
                    xtrem_index.append(i)
                    break

        return xtrem_index
