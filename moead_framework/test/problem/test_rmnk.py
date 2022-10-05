import random
import os
import unittest

from moead_framework.problem.combinatorial import Rmnk


class RmnkTest(unittest.TestCase):
    """Test the 'rmnk' problem."""

    def setUp(self):
        """Init"""
        self.project_path = os.path.dirname(os.path.abspath(__file__))
        self.problem = Rmnk(self.project_path + '/../data/instances/rmnk_0_2_100_1_0.dat')

    def test_instance_with_file(self):
        """Test constructor with instance file"""

        project_path = os.path.dirname(os.path.abspath(__file__))
        problem = Rmnk(project_path + '/../data/instances/rmnk_0_2_100_1_0.dat')
        self.assertEqual(problem.rho, 0)
        self.assertEqual(problem.m, 2)
        self.assertEqual(problem.n, 100)
        self.assertEqual(problem.k, 1)

    def test_instance_with_data(self):
        """Test constructor with data"""

        tables = [[0.07603153, 0.6942926, 0.5821437, 0.6527693],
                  [0.6255131, 0.6099211, 0.3105866, 0.5703756],
                  [0.6935567, 0.0896297, 0.5849524, 0.5712496],
                  [0.5399036, 0.2380261, 0.5293215, 0.5150103],
                  [0.7522732, 0.6271333, 0.4760139, 0.722034],
                  [0.2975375, 0.9355425, 0.37959, 0.937786],
                  [0.6182837, 0.7013475, 0.74283, 0.5226863],
                  [0.9722129, 0.1196809, 0.9520409, 0.6785079],
                  [0.8677718, 0.7736192, 0.01843654, 0.4930605],
                  [0.9008309, 0.9495603, 0.3262878, 0.5074039],
                  [0.6247835, 0.8236493, 0.9315534, 0.8588557],
                  [0.1586483, 0.7327879, 0.9168861, 0.0307912],
                  [0.3353818, 0.5943104, 0.1449176, 0.1876949],
                  [0.7321219, 0.01368841, 0.6006489, 0.9228483],
                  [0.5574075, 0.4177947, 0.01050017, 0.4578696],
                  [0.323836, 0.5307491, 0.6308105, 0.5138509],
                  [0.2154538, 0.01898192, 0.1521179, 0.1135412],
                  [0.890899, 0.1625834, 0.4129649, 0.928846],
                  [0.3011755, 0.5630689, 0.07151677, 0.7781862],
                  [0.6664792, 0.8228055, 0.5702866, 0.3438377],
                  [0.7678389, 0.2031639, 0.8864923, 0.8526771],
                  [0.07477007, 0.845149, 0.340179, 0.6484266],
                  [0.3411224, 0.04562186, 0.05630294, 0.6296429],
                  [0.9888505, 0.00625077, 0.2523649, 0.294141],
                  [0.5053455, 0.3049878, 0.5652824, 0.336989],
                  [0.07603153, 0.6942926, 0.5821437, 0.6527693],
                  [0.6255131, 0.6099211, 0.3105866, 0.5703756],
                  [0.6935567, 0.0896297, 0.5849524, 0.5712496],
                  [0.5399036, 0.2380261, 0.5293215, 0.5150103],
                  [0.7522732, 0.6271333, 0.4760139, 0.722034],
                  [0.2975375, 0.9355425, 0.37959, 0.937786],
                  [0.6182837, 0.7013475, 0.74283, 0.5226863],
                  [0.9722129, 0.1196809, 0.9520409, 0.6785079],
                  [0.8677718, 0.7736192, 0.01843654, 0.4930605],
                  [0.9008309, 0.9495603, 0.3262878, 0.5074039],
                  [0.6247835, 0.8236493, 0.9315534, 0.8588557],
                  [0.1586483, 0.7327879, 0.9168861, 0.0307912],
                  [0.3353818, 0.5943104, 0.1449176, 0.1876949],
                  [0.7321219, 0.01368841, 0.6006489, 0.9228483],
                  [0.5574075, 0.4177947, 0.01050017, 0.4578696],
                  [0.323836, 0.5307491, 0.6308105, 0.5138509],
                  [0.2154538, 0.01898192, 0.1521179, 0.1135412],
                  [0.890899, 0.1625834, 0.4129649, 0.928846],
                  [0.3011755, 0.5630689, 0.07151677, 0.7781862],
                  [0.6664792, 0.8228055, 0.5702866, 0.3438377],
                  [0.7678389, 0.2031639, 0.8864923, 0.8526771],
                  [0.07477007, 0.845149, 0.340179, 0.6484266],
                  [0.3411224, 0.04562186, 0.05630294, 0.6296429],
                  [0.9888505, 0.00625077, 0.2523649, 0.294141],
                  [0.5053455, 0.3049878, 0.5652824, 0.336989]
                  ]
        links = [
            [[0, 22],
             [1, 7],
             [2, 9],
             [3, 14],
             [4, 22],
             [5, 4],
             [6, 22],
             [7, 23],
             [8, 16],
             [9, 16],
             [10, 1],
             [11, 4],
             [12, 4],
             [13, 17],
             [14, 9],
             [15, 19],
             [16, 11],
             [17, 18],
             [18, 24],
             [19, 9],
             [20, 18],
             [21, 23],
             [22, 5],
             [23, 15],
             [24, 3]],
            [[0, 22],
             [1, 7],
             [2, 9],
             [3, 14],
             [4, 22],
             [5, 4],
             [6, 22],
             [7, 23],
             [8, 16],
             [9, 16],
             [10, 1],
             [11, 4],
             [12, 4],
             [13, 17],
             [14, 9],
             [15, 19],
             [16, 11],
             [17, 18],
             [18, 24],
             [19, 9],
             [20, 18],
             [21, 23],
             [22, 5],
             [23, 15],
             [24, 3]]
        ]
        rho = 0
        m = 2
        n = 25
        k = 1
        problem = Rmnk(rho=rho, m=m, n=n, k=k, links=links, tables=tables)
        self.assertEqual(problem.rho, 0)
        self.assertEqual(problem.m, 2)
        self.assertEqual(problem.n, 25)
        self.assertEqual(problem.k, 1)

    def test_generate_random_solution(self):
        """Test the function 'generate_random_solution'"""
        random_solution = self.problem.generate_random_solution()
        self.assertEqual(len(random_solution.decision_vector), 100)
        self.assertEqual(len(random_solution.F), 2)

        for item in random_solution.decision_vector:
            self.assertIn(item, [0, 1])

        for function_i in random_solution.F:
            self.assertLess(function_i, 0)
            self.assertGreater(function_i, -1)

    def test_generate_solution(self):
        """Test the function 'generate_solution'"""
        array = []

        for i in range(100):
            array.append(random.randint(0, 1))

        solution = self.problem.evaluate(array)
        self.assertEqual(len(solution.decision_vector), 100)
        self.assertEqual(len(solution.F), 2)

        for item in solution.decision_vector:
            self.assertIn(item, [0, 1])

        for function_i in solution.F:
            self.assertLess(function_i, 0)
            self.assertGreater(function_i, -1)

    def test_evaluation(self):
        """Test evaluation"""
        array = []

        for i in range(100):
            array.append(1)

        solution = self.problem.evaluate(array)

        self.assertEqual(solution.F[0], -0.4884468640000001)
        self.assertEqual(solution.F[1], -0.4930223456999998)

    def test_sad_path_parameters(self):
        with self.assertRaises(TypeError):
            self.problem = Rmnk(2)







