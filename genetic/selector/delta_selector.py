import random

from genetic.selector.abstract_selector import GeneticSelector


class DeltaSelector(GeneticSelector):
    def select(self, sub_problem):
        """
        delta is the probability that parent solutions are selected from the neighborhood
        :param sub_problem:
        :return:
        """
        rand = random.random()
        if rand < self.algorithm.delta:
            return self.algorithm.b[sub_problem]
        else:
            return list(range(self.algorithm.number_of_weight))
