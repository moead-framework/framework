import unittest
import random
import numpy as np

from moead_framework.core.genetic_operator.combinatorial import Crossover, BinaryMutation
from moead_framework.core.genetic_operator.numerical import DifferentialEvolutionCrossover, PolynomialMutation, \
    MoeadDeOperators
from moead_framework.problem.numerical import Zdt1


class GeneticOperatorsTest(unittest.TestCase):
    """Test genetic operators."""

    def setUp(self):
        """Init"""
        random.seed(1)
        np.random.seed(1)

    def test_combinatorial_binary_mutation(self):
        """Test combinatorial binary mutation"""
        array_solution = [1, 0, 0, 1, 1, 0]
        new_solution = BinaryMutation(solutions=[array_solution]).run()

        self.assertEqual(new_solution, [0, 0, 0, 1, 1, 0])

    def test_combinatorial_crossover(self):
        """Test combinatorial crossover multi-points"""
        array_solution1 = [1, 2, 3, 4, 5]
        array_solution2 = [6, 7, 8, 9, 10]
        new_solution_one_point = Crossover(solutions=[array_solution1, array_solution2],
                                           crossover_points=1).run().tolist()
        new_solution_three_point = Crossover(solutions=[array_solution1, array_solution2],
                                             crossover_points=3).run().tolist()

        self.assertEqual(new_solution_one_point, [1, 2, 8, 9, 10])
        self.assertEqual(new_solution_three_point, [1, 7, 8, 4, 10])

    def test_numerical_polynomial_mutation(self):
        """Test numerical polynomial mutation"""
        problem = Zdt1(20)
        array_solution = problem.generate_random_solution().solution
        new_solution = PolynomialMutation(solutions=[array_solution]).run()

        self.assertEqual(new_solution, [0.13890427141075934, 0.95236226912859, 0.750939942185552, 0.21601593072335035,
                                        0.4874043369178731, 0.32275331169490873, 0.6136038214883794, 0.782426788735786,
                                        0.0934591532089335, 0, 0.799635448887833, 0.39417267589080196,
                                        0.7582764986496935, 0, 0.30621673960609863, 0.7790024421369698,
                                        0.23504803024049092, 0.9627424572470192, 0.8554073901906575,
                                        0.22914795694915369])

    def test_numerical_de_crossover(self):
        """Test numerical de crossover"""
        problem = Zdt1(5)
        array_solution1 = problem.generate_random_solution().solution
        array_solution2 = problem.generate_random_solution().solution
        array_solution3 = problem.generate_random_solution().solution

        new_solution = DifferentialEvolutionCrossover(solutions=[array_solution1,
                                                                 array_solution2,
                                                                 array_solution3]).run()

        self.assertEqual(new_solution, [0, 0.9568466893460874, 0.7769962533153996,
                                        0.3009457924509838, 0.2869152283255434])

    def test_moead_de_operator(self):
        """Test numerical de crossover"""
        problem = Zdt1(5)
        array_solution1 = problem.generate_random_solution().solution
        array_solution2 = problem.generate_random_solution().solution
        array_solution3 = problem.generate_random_solution().solution

        new_solution = MoeadDeOperators(solutions=[array_solution1,
                                                   array_solution2,
                                                   array_solution3]).run()

        self.assertEqual(new_solution, [0.021382317860195066, 1, 0.7327909561319956,
                                        0.17080281343876919, 0.2590886275388289])
