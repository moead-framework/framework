import os

import unittest

from moead_framework.aggregation import Tchebycheff
from moead_framework.algorithm.combinatorial import Moead, MoeadDRA, MoeadSPSRandom

from moead_framework.core.sps_strategy import SpsDra, SpsRandomAndBoundaries
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

        delta = 0.9
        nr = 2

        self.moead_dra = MoeadDRA(problem=self.rmnk,
                                  max_evaluation=self.number_of_evaluations,
                                  number_of_objective=self.number_of_objective,
                                  number_of_weight_neighborhood=self.number_of_weight_neighborhood,
                                  number_of_crossover_points=self.number_of_crossover_points,
                                  aggregation_function=Tchebycheff,
                                  weight_file=self.weight_file,
                                  delta=delta,
                                  number_of_replacement=nr
                                  )
        self.moead_rdm = MoeadSPSRandom(problem=self.rmnk,
                                        max_evaluation=self.number_of_evaluations,
                                        number_of_objective=self.number_of_objective,
                                        aggregation_function=Tchebycheff,
                                        number_of_weight_neighborhood=self.number_of_weight_neighborhood,
                                        number_of_crossover_points=self.number_of_crossover_points,
                                        weight_file=self.weight_file,
                                        number_of_subproblem_to_visit=4)
        self.moead = Moead(problem=self.rmnk,
                           max_evaluation=self.number_of_evaluations,
                           number_of_objective=self.number_of_objective,
                           number_of_weight=self.number_of_weight,
                           aggregation_function=Tchebycheff,
                           number_of_weight_neighborhood=self.number_of_weight_neighborhood,
                           number_of_crossover_points=self.number_of_crossover_points,
                           weight_file=self.weight_file,
                           )

    def test_sps_dra1(self):
        """Test sps"""
        sps = SpsDra(algorithm_instance=self.moead_dra)
        sps_subproblems = sps.get_sub_problems()
        self.assertEqual(list(sps_subproblems), [8, 9])

    def test_sps_dra2(self):
        """Test sps"""
        sps = SpsDra(algorithm_instance=self.moead)
        with self.assertRaises(AttributeError):
            sps_subproblems = sps.get_sub_problems()

    def test_sps_SpsRandomAndBoundaries1(self):
        sps = SpsRandomAndBoundaries(algorithm_instance=self.moead_rdm)
        sps_subproblems = sps.get_sub_problems()
        self.assertEqual(list(sps_subproblems), [2, 1, 4, 6, 7, 8])

    def test_sps_SpsRandomAndBoundaries2(self):
        sps = SpsRandomAndBoundaries(algorithm_instance=self.moead)
        with self.assertRaises(AttributeError):
            sps_subproblems = sps.get_sub_problems()
