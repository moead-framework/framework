import unittest
import random
import os
import numpy as np
from moead_framework.aggregation import Tchebycheff
from moead_framework.algorithm.numerical import Moead
from moead_framework.problem.numerical import Zdt1
from moead_framework.tool.result import compute_hypervolume


class AlgorithmsNumericalTest(unittest.TestCase):
    """Test implemented algorithms."""

    def setUp(self):
        """Init"""
        random.seed(1)
        np.random.seed(1)
        self.number_of_evaluations = 100

        project_path = os.path.dirname(os.path.abspath(__file__))

        self.zdt1 = Zdt1(size=10)
        self.number_of_objective = 2
        self.number_of_weight = 10
        self.number_of_weight_neighborhood = 20
        self.weight_file = project_path + "/data/weights/SOBOL-" \
                           + str(self.number_of_objective) \
                           + "objs-" + str(self.number_of_weight) \
                           + "wei.ws"

    def test_numerical_moead(self):
        """Test MOEA/D algorithm with ZDT1"""

        moead = Moead(problem=self.zdt1,
                      max_evaluation=self.number_of_evaluations,
                      number_of_objective=self.number_of_objective,
                      number_of_weight=self.number_of_weight,
                      number_of_weight_neighborhood=self.number_of_weight_neighborhood,
                      weight_file=self.weight_file,
                      aggregation_function=Tchebycheff
                      )

        non_dominated = moead.run()
        self.assertEqual(len(non_dominated), 6)  # test the number of non_dominated solutions
        self.assertEqual(compute_hypervolume(non_dominated, [11, 11]), 91.30063166767695)  # test the hypervolume value
