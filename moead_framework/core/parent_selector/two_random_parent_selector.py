import random
from moead_framework.core.parent_selector.abstract_parent_selector import ParentSelector


class TwoRandomParentSelector(ParentSelector):
    """
    Select two parents randomly in the list of index
    """

    def select(self, indexes):
        """
        Select parents in the neighborhood represented by indexes

        :param indexes: {list<integer>} indexes of solutions used to select parents
        :return: {list<:class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`>} parents used to generate the future offspring
        """
        super().select(indexes=indexes)

        index1 = indexes[random.randint(0, len(indexes) - 1)]
        index2 = indexes[random.randint(0, len(indexes) - 1)]

        parent1 = self.algorithm.population[index1]
        parent2 = self.algorithm.population[index2]

        return [parent1, parent2]
