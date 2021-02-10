import os
import unittest

from moead_framework.problem.combinatorial import Mubqp


class UbqpTest(unittest.TestCase):
    """Test the 'rmnk' problem."""

    def setUp(self):
        """Init"""
        project_path = os.path.dirname(os.path.abspath(__file__))
        self.problem = Mubqp(project_path + '/../data/instances/mubqp_0_2_25_0.8_0.dat')

    def test_instance(self):
        """Test parameters"""
        self.assertEqual(self.problem.rho, 0)
        self.assertEqual(self.problem.m, 2)
        self.assertEqual(self.problem.n, 25)
        self.assertEqual(self.problem.d, 0.8)

    def test_generate_random_solution(self):
        """Test the function 'generate_random_solution'"""
        random_solution = self.problem.generate_random_solution()

        self.assertEqual(len(random_solution.solution), 25)
        self.assertEqual(len(random_solution.F), 2)

        for item in random_solution.solution:
            self.assertIn(item, [0, 1])

    def test_evaluation(self):
        """Test evaluation"""
        array = []

        for i in range(100):
            if i % 3 == 0:
                array.append(0)
            else:
                array.append(1)

        solution = self.problem.generate_solution(array)

        self.assertEqual(solution.F[0], -290.0)
        self.assertEqual(solution.F[1], -856.0)






