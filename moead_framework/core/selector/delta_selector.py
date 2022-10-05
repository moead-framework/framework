import random

from .abstract_selector import MatingPoolSelector


class DeltaSelector(MatingPoolSelector):
    """
    According to the probability delta (required attribute in the algorithm), the selector will select the neighborhood or the whole population.
    The attribute 'delta' represents the probability that parent solutions are selected from the neighborhood.
    """

    def __init__(self, algorithm_instance):
        """
        Constructor of the mating pool selector

        :param algorithm_instance: {:class:`~moead_framework.algorithm.abstract_moead.py.AbstractMoead`} instance of the algorithm
        """
        super().__init__(algorithm_instance)

        if not hasattr(self.algorithm, 'delta'):
            msg = "Algorithm lacks required attribute 'delta' for component 'DeltaSelector'. "
            raise AttributeError(msg)

    def select(self, sub_problem):
        """
        Select the mating pool.

        :param sub_problem: {integer} index of the current sub-problem visited
        :return: {list<integer>}
        """
        super().select(sub_problem=sub_problem)
        rand = random.random()
        if rand < self.algorithm.delta:
            return self.algorithm.b[sub_problem]
        else:
            return list(range(self.algorithm.number_of_weight))
