from .solution import Solution


class OneDimensionSolution(Solution):
    """
    Represent a one dimension solution for combinatorial and numerical problems
    """

    solution = []  #: :{list} all objectives values of the solution.
    F = []         #: :{list} all objectives values of the solution.
    distance = 0   #: :{integer} optional - can be used to compute a distance (crowding distance, ...)

    def __init__(self, solution, f=None):
        """
        Constructor of the solution

        :param solution: {list} all decision variables of the solution
        :param f: {list<float>} all objectives values of the solution. The default value is None if the solution is not evaluated.
        """
        super().__init__(solution, f)
        self.distance = 0

    def __repr__(self):
        return str(self.F)

    def __getitem__(self, index):
        return self.F[index]

    def __setitem__(self, index, value):
        self.F[index] = value

    def __copy__(self):
        return OneDimensionSolution(self.solution[:], self.F[:])
