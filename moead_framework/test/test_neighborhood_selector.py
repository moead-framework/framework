import os

import unittest

from moead_framework.aggregation import Tchebycheff
from moead_framework.algorithm.combinatorial import Moead, MoeadDeltaNr
from moead_framework.core.parent_selector import TwoRandomParentSelector, OneRandomAndCurrentParentSelector, \
    TwoRandomAndCurrentParentSelector
from moead_framework.core.selector import DeltaSelector
from moead_framework.problem.combinatorial import Rmnk
from moead_framework.tool.result import set_seed


class ParentSelectorTest(unittest.TestCase):
    """Test genetic operators."""

    def setUp(self):
        """Init"""
        set_seed(1)

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

        delta = 0.9
        nr = 2

        self.moead_delta_nr = MoeadDeltaNr(problem=self.rmnk,
                                           max_evaluation=self.number_of_evaluations,
                                           number_of_objective=self.number_of_objective,
                                           number_of_weight_neighborhood=self.number_of_weight_neighborhood,
                                           number_of_crossover_points=self.number_of_crossover_points,
                                           aggregation_function=Tchebycheff,
                                           weight_file=self.weight_file,
                                           delta=delta,
                                           number_of_replacement=nr
                                           )

    def test_delta_selector1(self):
        """Test delta selector"""
        ds = DeltaSelector(algorithm_instance=self.moead_delta_nr)
        select = ds.select(sub_problem=1)
        self.assertEqual(select, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_delta_selector2(self):
        """Test delta selector"""
        ds = DeltaSelector(algorithm_instance=self.moead_delta_nr)
        with self.assertRaises(TypeError):
            select = ds.select(sub_problem="1")

    def test_delta_selector3(self):
        """Test delta selector"""
        with self.assertRaises(AttributeError):
            ds = DeltaSelector(algorithm_instance=self.moead)
