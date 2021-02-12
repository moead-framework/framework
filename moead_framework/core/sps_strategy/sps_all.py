from moead_framework.core.sps_strategy.abstract_sps import SpsStrategy


class SpsAllSubproblems(SpsStrategy):
    """
    The classic SPS Strategy, all sub-problems are visited at each generation
    """

    def get_sub_problems(self):
        return range(self.algorithm.number_of_weight)
