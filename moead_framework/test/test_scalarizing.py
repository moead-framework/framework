import os
import unittest

from moead_framework.problem.combinatorial import Rmnk
from moead_framework.aggregation import Tchebycheff
from moead_framework.aggregation import WeightedSum
from moead_framework.tool.mop import generate_weight_vectors


class ScalarizingTest(unittest.TestCase):
    """Test aggregation functions."""

    def setUp(self):
        """Init"""
        project_path = os.path.dirname(os.path.abspath(__file__))
        self.problem = Rmnk(project_path + '/data/instances/rmnk_0_2_100_1_0.dat')
        weight_file = project_path + "/data/weights/SOBOL-2objs-10wei.ws"
        self.weights = generate_weight_vectors(weight_file, False)

        array = []

        for i in range(100):
            array.append(1)

        self.solution = self.problem.generate_solution(array)
        self.z = [1, 1]

    def test_tchebycheff(self):
        """Test Tchebycheff"""

        value1 = Tchebycheff().run(self.solution, 2, self.weights, 3, self.z)
        value2 = Tchebycheff().run(self.solution, 2, self.weights, 8, self.z)

        self.assertEqual(value1, 1.1197667592749998)
        self.assertEqual(value2, 1.3023910060000001)
        self.assertFalse(Tchebycheff().is_better(value1, value2))
        self.assertTrue(Tchebycheff().is_better(value2, value1))

    def test_weighted_sum(self):
        """Test Weighted Sum"""

        value1 = WeightedSum().run(self.solution, 2, self.weights, 3, self.z)
        value2 = WeightedSum().run(self.solution, 2, self.weights, 8, self.z)

        self.assertEqual(value1, -0.4918784752749999)
        self.assertEqual(value2, -0.4890187992125)
        self.assertFalse(WeightedSum().is_better(value1, value2))
        self.assertTrue(WeightedSum().is_better(value2, value1))



