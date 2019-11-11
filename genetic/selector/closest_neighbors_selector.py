from genetic.selector.abstract_selector import GeneticSelector


class ClosestNeighborsSelector(GeneticSelector):
    def select(self, sub_problem):
        return self.algorithm.b[sub_problem]
