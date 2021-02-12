from .abstract_selector import MatingPoolSelector


class ClosestNeighborsSelector(MatingPoolSelector):
    """
    Return indexes of solutions in the neighborhood according to the current sub-problem visited.
    """

    def select(self, sub_problem):
        """
        Select the mating pool.

        :param sub_problem: {integer} index of the current sub-problem visited
        :return: {list<integer>}
        """
        return self.algorithm.b[sub_problem]
