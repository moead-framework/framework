import random

from moead_framework.core.sps_strategy.abstract_sps import SpsStrategy


class SpsRandomAndBoundaries(SpsStrategy):
    """
    Select randomly lambda sub-problems at each generation with boundaries sub-problems

    Pruvost, Geoffrey, et al.
    "On the Combined Impact of Population Size and Sub-problem Selection in MOEA/D."
    European Conference on Evolutionary Computation in Combinatorial Optimization (Part of EvoStar).
    Springer, Cham, 2020

    The strategy requires the attribute number_of_subproblem to define the number of sub-problem to iterate for the next generation.

    """
    def get_sub_problems(self):
        """
        Select lambda random sub problems

        lambda is represented here by the attribute self.algorithm.number_of_subproblem

        :return: {list<integer>} indexes of sub-problems
        """
        if not hasattr(self.algorithm, 'number_of_subproblem'):
            msg = "Algorithm lacks required attribute 'number_of_subproblem' for component 'SpsRandomAndBoundaries'."
            raise AttributeError(msg)

        range_list = list(range(self.algorithm.number_of_weight))
        xtrem_index = self.get_xtrem_index()
        random_indexes = random.sample(list(set(range_list) - set(xtrem_index)), self.algorithm.number_of_subproblem)

        random_indexes = random_indexes + xtrem_index
        random.shuffle(random_indexes)

        return random_indexes
