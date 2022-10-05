import numpy as np
from moead_framework.problem.problem import Problem


class Rmnk(Problem):
    """
    Implementation of the multiobjective NK landscapes with tunable objective correlation.
    The problem is compatible with files generated
    by the mocobench generator http://mocobench.sourceforge.net/index.php?n=Problem.RMNK

    Example:

    >>> from moead_framework.problem.combinatorial import Rmnk
    >>>
    >>> # The file is available here : https://github.com/moead-framework/data/blob/master/problem/RMNK/Instances/rmnk_0_2_100_1_0.dat
    >>> # Others instances are available here : https://github.com/moead-framework/data/tree/master/problem/RMNK/Instances
    >>> instance_file = "moead_framework/test/data/instances/rmnk_0_2_100_1_0.dat"
    >>> rmnk = Rmnk(instance_file=instance_file)
    >>>
    >>> # Generate a new solution
    >>> solution = rmnk.generate_random_solution()
    >>>
    >>> # Print all decision variables of the solution
    >>> print(solution.decision_vector)
    >>>
    >>> # Print all objectives values of the solution
    >>> print(solution.F)
    """

    dtype = float

    def __init__(self, instance_file=None, rho=None, m=None, n=None, k=None, links=None, tables=None):
        f"""
        Constructor of the problem. 
        You can initialize the problem directly by using an instance file or by setting parameters : rho, m, n, k, links and tables. 
        http://mocobench.sourceforge.net/index.php?n=Problem.RMNK#Format

        :param instance_file: {str} text file generated by the rmnk generator : http://mocobench.sourceforge.net/index.php?n=Problem.RMNK#Code
        :param rho: {float} the objective correlation coefficient
        :param m: {int} the number of objective functions
        :param n: {int} the length of solutions
        :param k: {list} the number of epistatic links (non-linearity)
        :param links: {list} describe the epistatic structure between variables
        :param tables: {list} describe the fitness contribution
        """
        self.rho = None
        self.m = None
        self.n = None
        self.k = None
        self.links = None
        self.tables = None
        self.instance_file = None

        if instance_file is not None:
            if not isinstance(instance_file, str):
                raise TypeError("The expected type of `instance_file` is `str`")
            self.init_with_instance_file(instance_file=instance_file)
        elif (rho is not None) & (m is not None) & (n is not None) & (k is not None) & (links is not None) & (
                tables is not None):
            self.init_with_data(rho=rho, m=m, n=n, k=k, links=links, tables=tables)
        else:
            msg = "The constructor needs either the instance_file parameter or the following parameters : " \
                  "rho, m, n, k, links and tables."
            raise ValueError(msg)

        super().__init__(objective_number=self.m)

    def init_with_instance_file(self, instance_file):

        if isinstance(instance_file, str):
            self.instance_file = instance_file
        else:
            raise TypeError("The instance_file parameter must be a string.")

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

        file_content = file_content[line + 1:]
        self.load_tables(file_content)

        file.close()

    def init_with_data(self, rho, m, n, k, links, tables):

        if isinstance(m, int) & isinstance(n, int) & isinstance(k, int):
            self.m = m
            self.n = n
            self.k = k
        else:
            raise TypeError("The parameters m, n and k must be positive integers.")

        if isinstance(rho, (int, float)):
            self.rho = rho
        else:
            raise TypeError("The parameter rho must be a float.")

        if isinstance(links, list) & isinstance(tables, list):
            self.links = links
            self.tables = tables
        else:
            raise TypeError("The parameters links and tables must be list.")

    def f(self, function_id: int, decision_vector: np.ndarray):
        """
        Evaluate the decision_vector for the objective function_id

        :param function_id: {integer} index of the objective
        :param decision_vector: {:class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`} solution to evaluate
        :return: {float} fitness value
        """
        if not isinstance(function_id, int):
            raise TypeError("The expected type of `function_id` is `int`")

        if not isinstance(decision_vector, np.ndarray):
            raise TypeError("The expected type of `decision_vector` is `np.ndarray`")

        accu = 0

        for i in range(self.n):
            accu += self.tables[function_id][i][self.sigma(function_id, decision_vector, i)]

        return -1 * (accu / self.n)

    def sigma(self, function_id, solution_array, item):
        """
        Compute the sigma value

        :param function_id: {integer} index of the objective function
        :param solution_array: {list<integer>} representation of the solution
        :param item: {integer} index of the variable
        :return:
        """
        n = 1
        accu = 0

        for j in range(self.k + 1):
            link = int(self.links[function_id][item][j])
            if solution_array[link]:
                accu = accu | n

            n = n << 1

        return accu

    def generate_random_solution(self):
        """
        Generate a random solution for the current problem

        :return: {:class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`}
        """

        return self.evaluate(x=np.random.randint(0, 2, self.n).tolist()[:])

    def load_links(self, file_content):
        """
        Load links from the instance file

        :param file_content: {list<float>} content of the instance file
        :return: {integer} the number of line
        """
        line = 0
        for i in range(self.n):
            for j in range(self.k + 1):
                s = file_content[line].split("  ")
                line += 1
                for n in range(self.m):
                    self.links[n][i][j] = float(s[n])

        return line

    def load_tables(self, file_content):
        """
        Load tables from the instance file

        :param file_content: {list<float>} content of the instance file
        :return:
        """
        line = 0
        for i in range(self.n):
            for j in range(1 << (self.k + 1)):
                s = file_content[line].split("  ")
                line += 1
                for n in range(self.m):
                    self.tables[n][i][j] = float(s[n])
