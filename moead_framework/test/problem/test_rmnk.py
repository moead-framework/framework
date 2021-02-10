import random
import os
import unittest

from moead_framework.problem.combinatorial import Rmnk


class RmnkTest(unittest.TestCase):
    """Test the 'rmnk' problem."""

    def setUp(self):
        """Init"""
        project_path = os.path.dirname(os.path.abspath(__file__))
        self.problem = Rmnk(project_path + '/../data/instances/rmnk_0_2_100_1_0.dat')

    def test_instance(self):
        """Test parameters"""
        self.assertEqual(self.problem.rho, 0)
        self.assertEqual(self.problem.m, 2)
        self.assertEqual(self.problem.n, 100)
        self.assertEqual(self.problem.k, 1)

    def test_generate_random_solution(self):
        """Test the function 'generate_random_solution'"""
        random_solution = self.problem.generate_random_solution()
        self.assertEqual(len(random_solution.solution), 100)
        self.assertEqual(len(random_solution.F), 2)

        for item in random_solution.solution:
            self.assertIn(item, [0, 1])

        for function_i in random_solution.F:
            self.assertLess(function_i, 0)
            self.assertGreater(function_i, -1)

    def test_generate_solution(self):
        """Test the function 'generate_solution'"""
        array = []

        for i in range(100):
            array.append(random.randint(0, 1))

        solution = self.problem.generate_solution(array)
        self.assertEqual(len(solution.solution), 100)
        self.assertEqual(len(solution.F), 2)

        for item in solution.solution:
            self.assertIn(item, [0, 1])

        for function_i in solution.F:
            self.assertLess(function_i, 0)
            self.assertGreater(function_i, -1)

    def test_evaluation(self):
        """Test evaluation"""
        array = []

        for i in range(100):
            array.append(1)

        solution = self.problem.generate_solution(array)

        self.assertEqual(solution.F[0], -0.4884468640000001)
        self.assertEqual(solution.F[1], -0.4930223456999998)






