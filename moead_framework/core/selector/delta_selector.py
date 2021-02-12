import random

from .abstract_selector import MatingPoolSelector


class DeltaSelector(MatingPoolSelector):
    """
    According to the probability delta (attribute in the algorithm), the selector will select the neighborhood or the whole population.
    delta is the probability that parent solutions are selected from the neighborhood.
    """

    def select(self, sub_problem):
        """
        Select the mating pool.

        :param sub_problem: {integer} index of the current sub-problem visited
        :return: {list<integer>}
        """
        rand = random.random()
        if rand < self.algorithm.delta:
            return self.algorithm.b[sub_problem]
        else:
            return list(range(self.algorithm.number_of_weight))
