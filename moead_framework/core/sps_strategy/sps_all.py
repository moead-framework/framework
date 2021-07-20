from moead_framework.core.sps_strategy.abstract_sps import SpsStrategy


class SpsAllSubproblems(SpsStrategy):
    """
    The classic SPS Strategy, all sub-problems are visited at each generation
    """

    def get_sub_problems(self):
        """
        Get all sub-problems visited in the next generation

        :return: {list<integer>} indexes of sub-problems
        """
        return range(self.algorithm.number_of_weight)
