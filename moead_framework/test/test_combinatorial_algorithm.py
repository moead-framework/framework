import unittest
import random
import os
import numpy as np
from moead_framework.aggregation.tchebycheff import Tchebycheff
from moead_framework.algorithm.combinatorial import Moead, MoeadDeltaNr, MoeadSPSRandom, MoeadDRA
from moead_framework.problem.combinatorial import Rmnk
from moead_framework.tool.result import compute_hypervolume


class AlgorithmsTest(unittest.TestCase):
    """Test implemented algorithms."""

    def setUp(self):
        """Init"""
        random.seed(1)
        np.random.seed(1)
        self.number_of_evaluations = 100

        project_path = os.path.dirname(os.path.abspath(__file__))
        self.rmnk = Rmnk(instance_file=project_path + '/data/instances/rmnk_0_2_100_1_0.dat')

        self.number_of_objective = self.rmnk.number_of_objective
        self.number_of_weight = 10
        self.number_of_weight_neighborhood = 2
        self.number_of_crossover_points = 4
        self.weight_file = project_path + "/data/weights/SOBOL-" \
                           + str(self.number_of_objective) \
                           + "objs-" + str(self.number_of_weight) \
                           + "wei.ws"
        self.weight_file50 = project_path + "/data/weights/SOBOL-" \
                           + str(self.number_of_objective) \
                           + "objs-" + str(50) \
                           + "wei.ws"

    def test_moead(self):
        """Test MOEA/D algorithm"""

        moead = Moead(problem=self.rmnk,
                      max_evaluation=self.number_of_evaluations,
                      number_of_weight=self.number_of_weight,
                      aggregation_function=Tchebycheff,
                      number_of_weight_neighborhood=self.number_of_weight_neighborhood,
                      number_of_crossover_points=self.number_of_crossover_points,
                      weight_file=self.weight_file,
                      )

        non_dominated = moead.run()
        self.assertEqual(len(non_dominated), 8)  # test the number of non_dominated solutions
        self.assertEqual(compute_hypervolume(non_dominated, [0, 0]), 0.3079835420196539)  # test the hypervolume value

    def test_moead_delta_nr(self):
        """Test MOEA/D algorithm with parameters delta & nr"""
        delta = 0.9
        nr = 2

        moead = MoeadDeltaNr(problem=self.rmnk,
                             max_evaluation=self.number_of_evaluations,
                             number_of_objective=self.number_of_objective,
                             number_of_weight_neighborhood=self.number_of_weight_neighborhood,
                             number_of_crossover_points=self.number_of_crossover_points,
                             aggregation_function=Tchebycheff,
                             weight_file=self.weight_file,
                             delta=delta,
                             number_of_replacement=nr
                             )

        non_dominated = moead.run()

        self.assertEqual(len(non_dominated), 12)  # test the number of non_dominated solutions
        self.assertEqual(compute_hypervolume(non_dominated, [0, 0]), 0.3087417993003917)  # test the hypervolume value

    def test_moead_sps_random(self):
        """Test MOEA/D algorithm with the random sps strategy"""
        number_of_subproblem = 2
        moead = MoeadSPSRandom(problem=self.rmnk,
                               max_evaluation=self.number_of_evaluations,
                               number_of_objective=self.number_of_objective,
                               aggregation_function=Tchebycheff,
                               number_of_weight_neighborhood=self.number_of_weight_neighborhood,
                               number_of_crossover_points=self.number_of_crossover_points,
                               number_of_subproblem_to_visit=number_of_subproblem,
                               weight_file=self.weight_file,
                               )

        non_dominated = moead.run()

        self.assertEqual(len(non_dominated), 10)  # test the number of non_dominated solutions
        self.assertEqual(compute_hypervolume(non_dominated, [0, 0]), 0.30882255276025106)  # test the hypervolume value

    def test_moead_dra(self):
        """Test MOEA/D algorithm with the random sps strategy"""
        delta = 0.9
        nr = 2

        moead = MoeadDRA(problem=self.rmnk,
                         max_evaluation=500,
                         number_of_objective=self.number_of_objective,
                         number_of_weight_neighborhood=self.number_of_weight_neighborhood,
                         aggregation_function=Tchebycheff,
                         number_of_crossover_points=self.number_of_crossover_points,
                         weight_file=self.weight_file50,
                         delta=delta,
                         number_of_replacement=nr
                         )

        non_dominated = moead.run()

        self.assertEqual(len(non_dominated), 9)  # test the number of non_dominated solutions
        self.assertEqual(compute_hypervolume(non_dominated, [0, 0]), 0.3429102682198655)  # test the hypervolume value
