import random
import numpy as np
from moead_framework.core.genetic_operator.abstract_operator import GeneticOperator


class Crossover(GeneticOperator):

    def __init__(self, solution1, solution2, crossover_points=1):
        self.solution1 = solution1[:]
        self.solution2 = solution2[:]
        self.points = crossover_points

    def run(self):
        # random_int = random.randint(1, len(self.solution1) - 1)
        # p1 = self.solution1[0:random_int]
        # p2 = self.solution2[random_int:]
        # child = np.append(p1, p2)

        list_of_points = set()
        while len(list_of_points) < self.points:
            int_rand = random.randint(1, len(self.solution1) - 1)
            list_of_points.add(int_rand)

        list_of_points = sorted(list(list_of_points))

        current = 0
        last_i = 0
        child = []
        for i in range(self.points):
            last_i = i
            if i % 2 == 0:
                child = np.append(child, self.solution1[current:list_of_points[i]])
            else:
                child = np.append(child, self.solution2[current:list_of_points[i]])

            current = list_of_points[i]

            # todo : save the last i to know modulo to know how fill the rest of the child

        if last_i % 2 == 0:
            child = np.append(child, self.solution2[list_of_points[-1]:])
        else:
            child = np.append(child, self.solution1[list_of_points[-1]:])


        # print(str(self.points) + " point(s)")
        # print(self.solution1)
        # print("+")
        # print(self.solution2)
        # print("______________________")
        # print(child[:])
        # print()
        return child
