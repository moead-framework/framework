import random
import os
import unittest

from moead_framework.problem.combinatorial import KnapsackProblem


class KnapsackTest(unittest.TestCase):
    """Test the 'knapsack' problem."""

    def setUp(self):
        """Init"""
        self.project_path = os.path.dirname(os.path.abspath(__file__))
        number_of_objective = 2
        self.instance = self.project_path + '/../data/instances/MOKP_250_2.dat'
        self.problem = KnapsackProblem(number_of_objective=number_of_objective, instance_file=self.instance)

    def test_instance_file(self):
        """Test constructor with instance file"""
        project_path = os.path.dirname(os.path.abspath(__file__))

        problem = KnapsackProblem(number_of_objective=2, instance_file=project_path + '/../data/instances/MOKP_250_2.dat')
        self.assertEqual(problem.number_of_objective, 2)
        self.assertEqual(problem.number_of_objects, 250)

    def test_instance_data(self):
        """Test constructor with data"""
        weights = [[20, 11, 80, 50], [48, 19, 20, 38]]
        profits = [[2, 10, 73, 20], [34, 4, 83, 28]]
        capacities = [110, 90]

        problem = KnapsackProblem(number_of_objective=2, weights=weights, profits=profits, capacities=capacities)
        self.assertEqual(problem.number_of_objective, 2)
        self.assertEqual(problem.number_of_objects, 4)

    def test_generate_random_solution(self):
        """Test the function 'generate_random_solution'"""
        random_solution = self.problem.generate_random_solution()
        self.assertEqual(len(random_solution.decision_vector), 250)
        self.assertEqual(len(random_solution.F), 2)

        for item in random_solution.decision_vector:
            self.assertIn(item, [0, 1])

    def test_generate_solution(self):
        """Test the function 'generate_solution'"""
        array = []

        for i in range(250):
            array.append(random.randint(0, 1))

        solution = self.problem.evaluate(array)
        self.assertEqual(len(solution.decision_vector), 250)
        self.assertEqual(len(solution.F), 2)

        for item in solution.decision_vector:
            self.assertIn(item, [0, 1])

    def test_evaluation(self):
        """Test evaluation"""
        array = []

        for i in range(250):
            array.append(1)

        solution = self.problem.evaluate(array)

        self.assertEqual(solution.F[0], -75232.5)
        self.assertEqual(solution.F[1], -71644.4)

    def test_sad_path_parameters(self):
        with self.assertRaises(TypeError):
            self.problem = KnapsackProblem(number_of_objective="2", instance_file=self.instance)

        with self.assertRaises(TypeError):
            self.problem = KnapsackProblem(number_of_objective=2, instance_file=2)
