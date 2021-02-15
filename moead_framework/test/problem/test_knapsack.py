import random
import os
import unittest

from moead_framework.problem.combinatorial import KnapsackProblem


class RmnkTest(unittest.TestCase):
    """Test the 'rmnk' problem."""

    def setUp(self):
        """Init"""
        project_path = os.path.dirname(os.path.abspath(__file__))
        number_of_objective = 2
        instance = project_path + '/../data/instances/MOKP_250_2.dat'
        self.problem = KnapsackProblem(number_of_objective=number_of_objective, instance_file=instance)

    def test_instance(self):
        """Test parameters"""
        self.assertEqual(self.problem.number_of_objective, 2)
        self.assertEqual(self.problem.number_of_objects, 250)

    def test_generate_random_solution(self):
        """Test the function 'generate_random_solution'"""
        random_solution = self.problem.generate_random_solution()
        self.assertEqual(len(random_solution.solution), 250)
        self.assertEqual(len(random_solution.F), 2)

        for item in random_solution.solution:
            self.assertIn(item, [0, 1])

    def test_generate_solution(self):
        """Test the function 'generate_solution'"""
        array = []

        for i in range(250):
            array.append(random.randint(0, 1))

        solution = self.problem.generate_solution(array)
        self.assertEqual(len(solution.solution), 250)
        self.assertEqual(len(solution.F), 2)

        for item in solution.solution:
            self.assertIn(item, [0, 1])

    def test_evaluation(self):
        """Test evaluation"""
        array = []

        for i in range(250):
            array.append(1)

        solution = self.problem.generate_solution(array)

        self.assertEqual(solution.F[0], -75232.5)
        self.assertEqual(solution.F[1], -71644.4)
