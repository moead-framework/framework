from .abstract_selector import MatingPoolSelector


class ClosestNeighborsSelector(MatingPoolSelector):
    def select(self, sub_problem):
        return self.algorithm.b[sub_problem]
