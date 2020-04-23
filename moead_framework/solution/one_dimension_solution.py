from .solution import Solution


class OneDimensionSolution(Solution):
    solution = []
    distance = 0

    def __init__(self, solution, f=None):
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

