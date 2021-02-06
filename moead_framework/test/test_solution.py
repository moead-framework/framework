from copy import copy

import random
import os
import unittest

from moead_framework.problem.combinatorial import Rmnk


class RmnkTest(unittest.TestCase):
    """Test the 'rmnk' problem."""

    def setUp(self):
        """Init"""
        project_path = os.path.dirname(os.path.abspath(__file__))
        self.problem = Rmnk(project_path + '/data/instances/rmnk_0_2_100_1_0.dat')
        self.solution = self.problem.generate_random_solution()

    def test_set_item(self):
        """Test set item"""
        # todo
        self.assertEqual(self.solution[0], -0.5571641596999998)
        self.solution[0] = -42
        self.assertEqual(self.solution[0], -42)

    def test_repr(self):
        """Test repr'"""
        self.assertEqual(repr(self.solution), "[-0.5278004935999998, -0.4834306098]")

    def test_copy(self):
        """"Test the copy of solution"""
        copy_sol = copy(self.solution)
        # address are different
        self.assertNotEqual(copy_sol, self.solution)

        # solution are equals
        self.assertEqual(copy_sol.F, self.solution.F)
