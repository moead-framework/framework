import numpy as np
from moead_framework.problem.problem import Problem
from moead_framework.solution.one_dimension_solution import OneDimensionSolution


class Rmnk(Problem):

    def __init__(self, instance_file):
        file = open(instance_file, 'r')
        file_content = list(map(str.strip, file.readlines()))
        file_content = file_content[3:]

        definition = file_content[0].split(" ")
        self.rho = float(definition[2])
        self.m = int(definition[3])
        self.n = int(definition[4])
        self.k = int(definition[5])

        super().__init__(objective_number=self.m)

        self.links = np.zeros((self.m, self.n, self.k + 1))

        self.tables = np.zeros((self.m, self.n, 1 << (self.k + 1)))


        file_content = file_content[2:]
        line = self.load_links(file_content)

        file_content = file_content[line+1:]
        self.load_tables(file_content)

        file.close()

    def f(self, function_id, solution):
        accu = 0

        for i in range(self.n):
            accu += self.tables[function_id][i][self.sigma(function_id, solution, i)]

        return -1 * (accu / self.n)

    def sigma(self, function_id, solution_array, item):
        n = 1
        accu = 0

        for j in range(self.k + 1):
            link = int(self.links[function_id][item][j])
            if solution_array[link]:
                accu = accu | n

            n = n << 1

        return accu

    def generate_random_solution(self, evaluate=True):
        return self.generate_solution(array=np.random.randint(0, 2, self.n).tolist()[:], evaluate=evaluate)

    def generate_solution(self, array, evaluate=True):
        x = OneDimensionSolution(np.array(array, dtype=int))

        for j in range(self.function_numbers):
            if evaluate:
                x.F.append(self.f(j, x.solution))
            else:
                x.F.append(None)

        return x

    def load_links(self, array):
        line = 0
        for i in range(self.n):
            for j in range(self.k + 1):
                s = array[line].split("  ")
                line += 1
                for n in range(self.m):
                    self.links[n][i][j] = float(s[n])

        return line

    def load_tables(self, array):
        line = 0
        for i in range(self.n):
            for j in range(1 << (self.k + 1)):
                s = array[line].split("  ")
                line += 1
                for n in range(self.m):
                    self.tables[n][i][j] = float(s[n])
