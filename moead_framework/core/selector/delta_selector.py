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

        try:
            if not hasattr(self.algorithm, 'delta'):
                raise
        except Exception:
            msg = "The algorithm does not seem to be compatible with the component DeltaSelector. The parameter delta is required in the algorithm by the component DeltaSelector."
            raise ValueError(msg)

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
