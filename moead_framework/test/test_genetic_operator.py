import unittest
import random
import numpy as np

from moead_framework.core.genetic_operator.combinatorial.crossover import Crossover
from moead_framework.core.genetic_operator.combinatorial.mutation import BinaryMutation


class GeneticOperatorsTest(unittest.TestCase):
    """Test genetic operators."""

    def setUp(self):
        """Init"""
        random.seed(1)
        np.random.seed(1)

    def test_combinatorial_binary_mutation(self):
        """Test combinatorial binary mutation"""
        array_solution = [1, 0, 0, 1, 1, 0]
        new_solution = BinaryMutation(array_solution).run()

        self.assertEqual(new_solution, [1, 0, 0, 1, 1, 1])

    def test_combinatorial_crossover(self):
        """Test combinatorial crossover multi-points"""
        array_solution1 = [1, 2, 3, 4, 5]
        array_solution2 = [6, 7, 8, 9, 10]
        new_solution_one_point = Crossover(array_solution1, array_solution2, crossover_points=1).run().tolist()
        new_solution_three_point = Crossover(array_solution1, array_solution2, crossover_points=3).run().tolist()

        self.assertEqual(new_solution_one_point, [1, 2, 8, 9, 10])
        self.assertEqual(new_solution_three_point, [1, 7, 8, 4, 10])

