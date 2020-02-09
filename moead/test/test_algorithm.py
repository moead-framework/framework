import unittest
import random
import numpy as np
from moead.algorithm.moead import Moead
from moead.algorithm.moead_dra import MoeadDRA
from moead.algorithm.moead_delta_nr import MoeadDeltaNr
from moead.algorithm.moead_sps_random import MoeadSPSRandom
from moead.problem.rmnk import Rmnk
from moead.aggregation.tchebycheff import Tchebycheff
from moead.tool.result import compute_hypervolume


class AlgorithmsTest(unittest.TestCase):
    """Test implemented algorithms."""

    def setUp(self):
        """Init"""
        random.seed(1)
        np.random.seed(1)
        self.number_of_evaluations = 100

        instance_file = "moead/data/RMNK/Instances/rmnk_0_2_100_1_0.dat"
        self.rmnk = Rmnk(instance_file=instance_file)

        self.number_of_objective = self.rmnk.function_numbers
        self.number_of_weight = 10
        self.number_of_weight_neighborhood = 20
        self.number_of_crossover_points = 4
        self.weight_file = "moead/data/weights/SOBOL-" \
                           + str(self.number_of_objective) \
                           + "objs-" + str(self.number_of_weight) \
                           + "wei.ws"

    def test_moead(self):
        """Test MOEA/D algorithm"""

        moead = Moead(problem=self.rmnk,
                      max_evaluation=self.number_of_evaluations,
                      number_of_objective=self.number_of_objective,
                      number_of_weight=self.number_of_weight,
                      number_of_weight_neighborhood=self.number_of_weight_neighborhood,
                      number_of_crossover_points=self.number_of_crossover_points,
                      weight_file=self.weight_file,
                      )

        non_dominated = moead.run(g=Tchebycheff())
        self.assertEqual(len(non_dominated), 5)  # test the number of non_dominated solutions
        self.assertEqual(compute_hypervolume(non_dominated, [0, 0]), 0.33248710736231335)  # test the hypervolume value

    def test_moead_delta_nr(self):
        """Test MOEA/D algorithm with parameters delta & nr"""
        delta = 0.9
        nr = 2

        moead = MoeadDeltaNr(problem=self.rmnk,
                             max_evaluation=self.number_of_evaluations,
                             number_of_objective=self.number_of_objective,
                             number_of_weight=self.number_of_weight,
                             number_of_weight_neighborhood=self.number_of_weight_neighborhood,
                             number_of_crossover_points=self.number_of_crossover_points,
                             weight_file=self.weight_file,
                             delta=delta,
                             number_of_replacement=nr
                             )

        non_dominated = moead.run(g=Tchebycheff())

        self.assertEqual(len(non_dominated), 6)  # test the number of non_dominated solutions
        self.assertEqual(compute_hypervolume(non_dominated, [0, 0]), 0.3200990921863723)  # test the hypervolume value

    def test_moead_sps_random(self):
        """Test MOEA/D algorithm with the random sps strategy"""
        number_of_subproblem = 2
        moead = MoeadSPSRandom(problem=self.rmnk,
                               max_evaluation=self.number_of_evaluations,
                               number_of_objective=self.number_of_objective,
                               number_of_weight=self.number_of_weight,
                               number_of_weight_neighborhood=self.number_of_weight_neighborhood,
                               number_of_crossover_points=self.number_of_crossover_points,
                               number_of_subproblem=number_of_subproblem,
                               weight_file=self.weight_file,
                               )

        non_dominated = moead.run(g=Tchebycheff())

        self.assertEqual(len(non_dominated), 7)  # test the number of non_dominated solutions
        self.assertEqual(compute_hypervolume(non_dominated, [0, 0]), 0.35397501867058484)  # test the hypervolume value

    def test_moead_dra(self):
        """Test MOEA/D algorithm with the random sps strategy"""
        delta = 0.9
        nr = 2
        moead = MoeadDRA(problem=self.rmnk,
                         max_evaluation=self.number_of_evaluations,
                         number_of_objective=self.number_of_objective,
                         number_of_weight=self.number_of_weight,
                         number_of_weight_neighborhood=self.number_of_weight_neighborhood,
                         number_of_crossover_points=self.number_of_crossover_points,
                         weight_file=self.weight_file,
                         delta=delta,
                         number_of_replacement=nr
                         )

        non_dominated = moead.run(g=Tchebycheff())

        self.assertEqual(len(non_dominated), 6)  # test the number of non_dominated solutions
        self.assertEqual(compute_hypervolume(non_dominated, [0, 0]), 0.3200990921863723)  # test the hypervolume value