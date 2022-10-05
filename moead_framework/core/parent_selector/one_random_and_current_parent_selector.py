import random
from moead_framework.core.parent_selector.abstract_parent_selector import ParentSelector


class OneRandomAndCurrentParentSelector(ParentSelector):
    """
    Select two parents: one random solution in the list of index available and the solution in the population linked to the current sub-problem visited.
    """

    def select(self, indexes):
        """
        Select parents in the neighborhood represented by indexes

        :param indexes: {list<integer>} indexes of solutions used to select parents
        :return: {list<:class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`>} parents used to generate the future offspring
        """
        super().select(indexes=indexes)

        index2 = indexes[random.randint(0, len(indexes) - 1)]

        parent1 = self.algorithm.population[self.algorithm.current_sub_problem]
        parent2 = self.algorithm.population[index2]

        return [parent1, parent2]
