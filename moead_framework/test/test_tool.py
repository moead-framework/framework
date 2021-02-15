import unittest
import random
import os
import numpy as np
from moead_framework.problem.combinatorial import Rmnk
from moead_framework.tool.mop import get_non_dominated, population_size_without_duplicate, compute_crowding_distance
from moead_framework.tool.result import save_population, save_population_full, compute_hypervolume


class ToolsTest(unittest.TestCase):
    """Test implemented algorithms."""

    def setUp(self):
        """Init"""
        random.seed(1)
        np.random.seed(1)
        project_path = os.path.dirname(os.path.abspath(__file__))
        self.rmnk = Rmnk(instance_file=project_path + '/data/instances/rmnk_0_2_100_1_0.dat')
        self.rmnk3D = Rmnk(instance_file=project_path + '/data/instances/rmnk_0_3_100_1_0.dat')
        self.number_of_objective = self.rmnk.number_of_objective

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

    def test_population_size_without_duplicate(self):
        """test the function population_size_without_duplicate"""
        population = []

        for i in range(10):
            population.append(self.rmnk.generate_random_solution())

        # duplicate two solutions in the population
        population.append(population[4])
        population.append(population[2])

        self.assertEqual(len(population), 12)
        self.assertEqual(population_size_without_duplicate(population=population), 10)

    def test_hypervolume3D(self):
        """test the hypervolume in 3D"""
        population = []

        for i in range(10):
            population.append(self.rmnk3D.generate_random_solution())

        self.assertEqual(compute_hypervolume(population, [0, 0, 0]), 0.16108679722159508)  # test the hypervolume value

    def test_compute_crowding_distance(self):
        """test the function compute_crowding_distance"""
        population = []

        for i in range(10):
            population.append(self.rmnk.generate_random_solution())

        # distance equal to 0 before computing
        self.assertEqual(population[0].distance, 0)

        # compute the crowding distance
        pop_with_distance = compute_crowding_distance(population)

        self.assertEqual(population[0].distance, 0.07806191187999945)
        self.assertEqual(pop_with_distance[0].distance, 0.07806191187999945)

    def test_save_population(self):
        """test the function to save the population"""
        population = []

        for i in range(10):
            population.append(self.rmnk.generate_random_solution())

        save_population("test_save_population.txt", population)
        f = open("test_save_population.txt", "r")

        index_pop = 0
        for line in f:
            f1 = float(line.replace("\n", "").split(" ")[0])
            f2 = float(line.replace("\n", "").split(" ")[1])
            self.assertEqual(f1, population[index_pop].F[0])
            self.assertEqual(f2, population[index_pop].F[1])
            index_pop += 1

        f.close()
        os.remove("test_save_population.txt")

    def test_save_population_full(self):
        """test the function to save the population with all decision variables"""
        population = []

        for i in range(10):
            population.append(self.rmnk.generate_random_solution())

        save_population_full("test_save_population_full.txt", population)
        f = open("test_save_population_full.txt", "r")

        index_pop = 0
        for line in f:
            f1 = float(line.replace("\n", "").replace(" ", "_", 2).split("_")[0])
            f2 = float(line.replace("\n", "").replace(" ", "_", 2).split("_")[1])
            solution = line.replace("\n", "").replace(" ", "_", 2).split("_")[2]

            self.assertEqual(f1, population[index_pop].F[0])
            self.assertEqual(f2, population[index_pop].F[1])
            self.assertEqual(solution, str(population[index_pop].solution.tolist()))
            index_pop += 1

        f.close()
        os.remove("test_save_population_full.txt")
