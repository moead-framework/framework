from .base import Solution
from typing import List


class OneDimensionSolution(Solution):
    """
    Represent a one dimension solution for combinatorial and numerical problems
    """

    solution: List[float] = []  #: :{list} all decision variables of the solution.
    F: List[float] = []       #: :{list} all objectives values of the solution.
    distance = 0   #: :{integer} optional - can be used to compute a distance (crowding distance, ...)

    def __init__(self, decision_vector, f=None):
        """
        Constructor of the solution

        :param decision_vector: {list} all decision variables of the solution
        :param f: {list<float>} all objectives values of the solution. The default value is None if the solution is not evaluated.
        """
        super().__init__(decision_vector, f)
        self.distance = 0

    def __str__(self):
        return "Solution(F(x)=" + str(self.F) + " ; x=" +str(list(self.decision_vector)) + ")"

    def __repr__(self):
        return f'OneDimensionSolution(decision_vector={list(self.decision_vector)}, f={self.F})'

    def __getitem__(self, index):
        return self.F[index]

    def __setitem__(self, index, value):
        self.F[index] = value

    def __copy__(self):
        return OneDimensionSolution(self.decision_vector[:], self.F[:])
