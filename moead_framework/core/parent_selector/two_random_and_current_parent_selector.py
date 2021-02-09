import random
from moead_framework.core.parent_selector.abstract_parent_selector import ParentSelector


class TwoRandomAndCurrentParentSelector(ParentSelector):
    """
    Select three parents: two random solutions in the list of index and the solution in the population linked to the current sub-problem visited.
    """

    def select(self, indexes):
        index2 = indexes[random.randint(0, len(indexes) - 1)]
        index3 = indexes[random.randint(0, len(indexes) - 1)]

        parent1 = self.algorithm.population[self.algorithm.current_sub_problem]
        parent2 = self.algorithm.population[index2]
        parent3 = self.algorithm.population[index3]

        return [parent1, parent2, parent3]
