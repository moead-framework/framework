class Solution:

    def __init__(self, decision_vector, f=None):
        if f is None:
            f = []
        self.decision_vector = decision_vector
        self.F = f
