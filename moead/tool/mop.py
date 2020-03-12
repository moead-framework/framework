import random

import numpy as np
import pygmo as pg


def get_non_dominated(population, number_of_objective):
    """
    return all non dominated solutions of the population
    :param number_of_objective: integer
    :param population: list of solution
    :return: list of solution
    """
    to_remove = []

    if len(population) > 1:
        arr = []
        for s in population:
            arr.append(s.F)

        if number_of_objective == 2:
            new_pop = list(population[i] for i in pg.non_dominated_front_2d(arr))
        else:
            ndf, dl, dc, ndr = pg.fast_non_dominated_sorting(arr)
            new_pop = list(population[i] for i in ndf[0])

    else:
        for i in range(len(population)):
            for j in range(len(population)):
                nb_dominated_functions = 0
                for objective in range(number_of_objective):
                    if population[i].F[objective] > population[j].F[objective]:
                        nb_dominated_functions += 1

                if nb_dominated_functions == number_of_objective:
                    to_remove.append(population[i])

        new_pop = list(set(population).difference(set(to_remove)))

    return new_pop


def is_duplicated(x, population, number_of_objective):
    """
    identify if the solution x is already in the population
    :param number_of_objective: integer
    :param x: solution
    :param population: list of solution
    :return: boolean
    """
    for sol in population:
        is_dup = True
        for i in range(number_of_objective):
            if sol.F[i] != x.F[i]:
                is_dup = False
                break

        if is_dup:
            return True

    return False


def population_size_without_duplicate(population):
    """
    compute the population size without duplicate
    :param population:
    :return: integer
    """
    arr = []
    for ind in population:
        is_dup = False
        for ind_not_dup in arr:
            if np.array_equal(np.array(ind.solution), np.array(ind_not_dup.solution)):
                is_dup = True

        if not is_dup:
            arr.append(ind)

    return len(arr)


def compute_crowding_distance(s):
    """
    1. Get the number of nondominated solutions in the external repository
        a. n = | S |
    2. Initialize distance
        a. FOR i=0 TO MAX
            b. S[i].distance = 0
    3. Compute the crowding distance of each solution
        a. For each objective m
            b. Sort using each objective value
               S = sort(S, m)
            c. For i=1 to (n-1)
                d. S[i].distance = S[i].distance + (S[i+1].m – S[i-1].m)
        e. Set the maximum distance to the boundary points so that they are always selected
           S[0].distance = S[n].distance = maximum distance

        :param s:
        :return: s with computed distances
        """
    for individual in s:
        individual.distance = 0

    max_distance = 0
    for m in range(len(s[0].F)):
        s.sort(key=lambda x: x[m])

        for i in range(1, len(s) - 1):
            s[i].distance = s[i].distance + (s[i + 1][m] - s[i - 1][m])
            max_distance = max(max_distance, s[i].distance)

    s[0].distance = max_distance
    s[len(s) - 1].distance = max_distance

    return s


def generate_weight_vectors(weight_file, shuffle=True):
    file = open(weight_file, 'r')
    file_content = list(map(str.strip, file.readlines()))
    weights = []
    for row in file_content:
        weights.append(np.array(row.split(" ")).astype(np.float))

    if shuffle:
        random.shuffle(weights)

    file.close()
    return weights
