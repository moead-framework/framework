from moead_framework.core.sps_strategy.abstract_sps import SpsStrategy


class SpsAllSubproblems(SpsStrategy):
    """
    It is the classic SPS Strategy of MOEA/D, we visit all sub-problems at each generation
    """
    def get_sub_problems(self):
        return range(self.algorithm.number_of_weight)
