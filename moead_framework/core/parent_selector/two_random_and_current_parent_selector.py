import random
from moead_framework.core.parent_selector.abstract_parent_selector import ParentSelector


class TwoRandomAndCurrentParentSelector(ParentSelector):

    def select(self, indexes):
        index2 = indexes[random.randint(0, len(indexes) - 1)]
        index3 = indexes[random.randint(0, len(indexes) - 1)]

        parent1 = self.algorithm.population[self.algorithm.current_sub_problem]
        parent2 = self.algorithm.population[index2]
        parent3 = self.algorithm.population[index3]

        return [parent1, parent2, parent3]
