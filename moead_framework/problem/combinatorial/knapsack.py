import numpy as np
from moead_framework.problem.problem import Problem
from moead_framework.solution.one_dimension_solution import OneDimensionSolution


class KnapsackProblem(Problem):
    """
    Implementation of the Multiobjective knapsack problem by Thibaut Lust.
    The problem is compatible with files available on the
    author website: http://www-desir.lip6.fr/~lustt/Research.html#MOKP
    """
    def __init__(self, number_of_objective, instance_file):
        """
        Constructor of the problem

        :param number_of_objective: {integer}
        :param instance_file: {string} txt file of the instance: http://www-desir.lip6.fr/~lustt/Research.html#MOKP
        """
        super().__init__(number_of_objective)

        self.instance_file = instance_file
        self.weights = []
        self.profits = []
        self.capacities = []
        file = open(self.instance_file, 'r')
        file_content = list(map(str.strip, file.readlines()))
        file_content = file_content[2:]

        index_to_split_one = file_content.index("=")
        indexes_to_split = [index_to_split_one]
        for i in range(1, self.number_of_objective - 1):
            indexes_to_split.append(index_to_split_one * (i+1) + 1)

        kps = np.split(np.array(file_content), indexes_to_split)

        for kp in kps:
            if kp[0] == "=":
                kp = kp[1:]
            self.capacities.append(int(kp[1].replace("capacity: +", "")))
            w = []
            p = []
            for item in kp[2:]:
                if "weight" in item:
                    w.append(int(item.replace("weight: +", "")))
                if "profit" in item:
                    p.append(int(item.replace("profit: +", "")))

            self.weights.append(w)
            self.profits.append(p)

        self.number_of_objects = len(self.weights[0])
        file.close()

    def f(self, function_id, solution):
        function_id = function_id - 1
        weight = self.weight_of_solution(function_id, solution)
        profit = self.profit_of_solution(function_id, solution)

        if weight <= self.capacities[function_id]:
            return -profit  # minimize the profit
        else:
            return -profit - self.penality(function_id) * (weight - self.capacities[function_id]) # minimize the profit

    def profit_of_solution(self, function_id, solution):
        """
        Return the profit of the solution for the objective function_id

        :param function_id: {integer} index of the objective function
        :param solution: {list<integer>} representation of the solution
        :return: {float} profit of the solution
        """
        res = 0
        for i in range(0, self.number_of_objects):
            res += (self.profits[function_id][i] * solution[i])

        return res

    def weight_of_solution(self, function_id, solution):
        """
        Return the weight of the solution for the objective function_id

        :param function_id: {integer} index of the objective function
        :param solution: {list<integer>} representation of the solution
        :return: {float} weight of the solution
        """
        res = 0
        for i in range(0, self.number_of_objects):
            res += (self.weights[function_id][i] * solution[i])

        return res

    def penality(self, function_id):
        """
        Compute the penality for the specific objective

        :param function_id: {integer} index of the objective function
        :return: {float} penality value
        """
        max_founded = 0
        for i in range(0, self.number_of_objects):
            tmp = self.profits[function_id][i] / self.weights[function_id][i]
            if tmp > max_founded:
                max_founded = tmp

        return max_founded

    def generate_random_solution(self, evaluate=True):
        return self.generate_solution(array=np.random.randint(0, 2, self.number_of_objects).tolist()[:], evaluate=evaluate)

    def generate_solution(self, array, evaluate=True):
        x = OneDimensionSolution(array)

        for j in range(self.number_of_objective):
            if evaluate:
                x.F.append(self.f(j, x.solution))
            else:
                x.F.append(None)

        return x
