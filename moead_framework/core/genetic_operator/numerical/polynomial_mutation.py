import random
from moead_framework.core.genetic_operator.abstract_operator import GeneticOperator


class PolynomialMutation(GeneticOperator):
    """
    Polynomial Mutation operator.

    Require only one solution.
    """

    def run(self):
        self.number_of_solution_is_correct(n=1)
        solution = self.solutions[0]

        return self.mutation(s=solution, rate=1/len(solution), n=len(solution))

    def repair(self, s, mini=0, maxi=1):
        """
        Repair function for solutions

        :param s: solution's representation (In algorithms, it is represented by the attribute :class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution.solution` of the class :class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`)
        :param mini: {float} minimum value of variables in the solution
        :param maxi: {float} maximum value of variables in the solution
        :return:
        """
        return [mini if x < mini else maxi if x > maxi else x for x in s]

    def mutation(self, s, rate, n=20, mini=0, maxi=1):
        """
        Compute the polynomial mutation

        :param s: solution's representation (In algorithms, it is represented by the attribute :class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution.solution` of the class :class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`)
        :param rate: {float} mutation rate
        :param n: {integer} value used to compute the sigma value
        :param mini: {float} minimum value of variables in the solution
        :param maxi: {float} maximum value of variables in the solution
        :return:
        """
        rand = random.uniform(0, 1)
        return self.repair([s[x] if rand > rate else s[x] + self.sigma(n) * (maxi - (mini)) for x in range(len(s))])

    def sigma(self, n):
        """
        Compute the sigma value

        :param n: {integer}
        :return: {float}
        """
        rand = random.uniform(0, 1)
        sigma = 0
        if rand < 0.5:
            sigma = pow(2 * rand, 1 / (n + 1)) - 1
        else:
            sigma = 1 - pow(2 - 2 * rand, 1 / (n - 1))
        return sigma
