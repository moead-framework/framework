import random
from moead_framework.core.parent_selector.abstract_parent_selector import ParentSelector


class TwoRandomParentSelector(ParentSelector):
    """
    Select two parents randomly in the list of index
    """

    def select(self, indexes):
        index1 = indexes[random.randint(0, len(indexes) - 1)]
        index2 = indexes[random.randint(0, len(indexes) - 1)]

        parent1 = self.algorithm.population[index1]
        parent2 = self.algorithm.population[index2]

        return [parent1, parent2]
