import random

from moead_framework.core.sps_strategy.abstract_sps import SpsStrategy


class SpsRandomAndBoundaries(SpsStrategy):
    """
    Select randomly lambda sub-problems at each generation with boundaries sub-problems

    Pruvost, Geoffrey, et al.
    "On the Combined Impact of Population Size and Sub-problem Selection in MOEA/D."
    European Conference on Evolutionary Computation in Combinatorial Optimization (Part of EvoStar).
    Springer, Cham, 2020
    """
    def get_sub_problems(self):
        """
        Select lambda random sub problems in each cluster

        lambda is represented here by the attribute self.algorithm.number_of_subproblem

        :return: {list<integer>} indexes of sub-problems
        """
        range_list = list(range(self.algorithm.number_of_weight))
        xtrem_index = self.get_xtrem_index()
        random_indexes = random.sample(list(set(range_list) - set(xtrem_index)), self.algorithm.number_of_subproblem)

        random_indexes = random_indexes + xtrem_index
        random.shuffle(random_indexes)

        return random_indexes

    def get_xtrem_index(self):
        """
        get boundaries sub-problems

        :return: {list<integer>} indexes of sub-problems
        """
        xtrem_index = []
        for i in range(self.algorithm.number_of_weight):
            weight = self.algorithm.weights[i]
            for j in range(self.algorithm.number_of_objective):
                if weight[j] == 1:
                    xtrem_index.append(i)
                    break

        return xtrem_index
