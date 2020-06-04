import unittest
import random
import os
import numpy as np
from moead_framework.problem.combinatorial.rmnk import Rmnk
from moead_framework.tool.mop import get_non_dominated


class ToolsTest(unittest.TestCase):
    """Test implemented algorithms."""

    def setUp(self):
        """Init"""
        random.seed(1)
        np.random.seed(1)
        project_path = os.path.dirname(os.path.abspath(__file__))
        self.rmnk = Rmnk(instance_file=project_path + '/data/RMNK/Instances/rmnk_0_2_100_1_0.dat')
        self.number_of_objective = self.rmnk.function_numbers

    def test_PF(self):
        """Test get Non dominated"""
        solutions = []
        for i in range(20):
            solutions.append(self.rmnk.generate_random_solution())

        non_dominated_pop = get_non_dominated(population=solutions)
        non_dominated = []
        for s in non_dominated_pop:
            non_dominated.append(s.F)

        test = [[-0.5571641596999998, -0.4450894643], [-0.5483895551199999, -0.48251202308000013],
                [-0.5428439510999998, -0.48726908450000017], [-0.5107130364200001, -0.5078202645999998],
                [-0.5070678622999999, -0.5411136235], [-0.4660221059999998, -0.5569167061000001],
                [-0.4493039854199998, -0.5587430658000001]]

        self.assertEqual(len(non_dominated), len(test))

        for elt in test:
            self.assertIn(elt, non_dominated)
