class Solution:

    def __init__(self, solution, f=None):
        if f is None:
            f = []
        self.solution = solution
        self.F = f
