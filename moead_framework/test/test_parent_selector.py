import os

import unittest
import random
import numpy as np

from moead_framework.aggregation import Tchebycheff
from moead_framework.algorithm.combinatorial import Moead
from moead_framework.core.parent_selector import TwoRandomParentSelector, OneRandomAndCurrentParentSelector, \
    TwoRandomAndCurrentParentSelector
from moead_framework.problem.combinatorial import Rmnk


class ParentSelectorTest(unittest.TestCase):
    """Test genetic operators."""

    def setUp(self):
        """Init"""
        random.seed(1)
        np.random.seed(1)

        self.number_of_evaluations = 100

        project_path = os.path.dirname(os.path.abspath(__file__))
        self.rmnk = Rmnk(instance_file=project_path + '/data/instances/rmnk_0_2_100_1_0.dat')

        self.number_of_objective = self.rmnk.number_of_objective
        self.number_of_weight = 10
        self.number_of_weight_neighborhood = 10
        self.number_of_crossover_points = 4
        self.weight_file = project_path + "/data/weights/SOBOL-" \
                           + str(self.number_of_objective) \
                           + "objs-" + str(self.number_of_weight) \
                           + "wei.ws"

        self.moead = Moead(problem=self.rmnk,
                           max_evaluation=self.number_of_evaluations,
                           number_of_objective=self.number_of_objective,
                           number_of_weight=self.number_of_weight,
                           aggregation_function=Tchebycheff,
                           number_of_weight_neighborhood=self.number_of_weight_neighborhood,
                           number_of_crossover_points=self.number_of_crossover_points,
                           weight_file=self.weight_file,
                           )

    def test_two_random(self):
        """Test two random parent selector"""
        parent_selector = TwoRandomParentSelector(algorithm=self.moead)
        parents = parent_selector.select(self.moead.b[3])

        self.assertEqual(len(parents), 2)
        self.assertEqual(parents[0].F, [-0.48094203549999986, -0.52762151308])
        self.assertEqual(parents[1].F, [-0.5278004935999998, -0.4834306098])

    def test_one_random_and_current_parent(self):
        """Test one random and current parent selector"""
        parent_selector = OneRandomAndCurrentParentSelector(algorithm=self.moead)
        parents = parent_selector.select(self.moead.b[3])

        self.assertEqual(len(parents), 2)
        self.assertEqual(parents[0].F, [-0.4891762861, -0.5095645170000003])
        self.assertEqual(parents[1].F, [-0.48094203549999986, -0.52762151308])

    def test_two_random_and_current_parent(self):
        """Test two random and current parent selector"""
        parent_selector = TwoRandomAndCurrentParentSelector(algorithm=self.moead)
        parents = parent_selector.select(self.moead.b[3])

        self.assertEqual(len(parents), 3)
        self.assertEqual(parents[0].F, [-0.4891762861, -0.5095645170000003])
        self.assertEqual(parents[1].F, [-0.48094203549999986, -0.52762151308])
        self.assertEqual(parents[2].F, [-0.5278004935999998, -0.4834306098])
