from copy import copy

import os
import unittest

from moead_framework.problem.combinatorial import Rmnk
from moead_framework.tool.result import set_seed


class SolutionTest(unittest.TestCase):
    """Test the Solution class."""

    def setUp(self):
        """Init"""
        set_seed(1)
        project_path = os.path.dirname(os.path.abspath(__file__))
        self.problem = Rmnk(project_path + '/data/instances/rmnk_0_2_100_1_0.dat')
        self.solution = self.problem.generate_random_solution()

    def test_set_item(self):
        """Test set item"""
        self.assertEqual(self.solution[0], -0.5107130364200001)
        self.solution[0] = -42
        self.assertEqual(self.solution[0], -42)

    def test_repr(self):
        """Test repr'"""
        str_repr = "OneDimensionSolution(decision_vector=[1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0], f=[-0.5107130364200001, -0.5078202645999998])"
        self.assertEqual(repr(self.solution), str_repr)

    def test_copy(self):
        """"Test the copy of solution"""
        copy_sol = copy(self.solution)
        # address are different
        self.assertNotEqual(copy_sol, self.solution)

        # solution are equals
        self.assertEqual(copy_sol.F, self.solution.F)
