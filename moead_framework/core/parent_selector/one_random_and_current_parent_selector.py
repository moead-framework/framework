import random
from moead_framework.core.parent_selector.abstract_parent_selector import ParentSelector


class OneRandomAndCurrentParentSelector(ParentSelector):

    def select(self, indexes):
        index2 = indexes[random.randint(0, len(indexes) - 1)]

        parent1 = self.algorithm.population[self.algorithm.current_sub_problem]
        parent2 = self.algorithm.population[index2]

        return [parent1, parent2]