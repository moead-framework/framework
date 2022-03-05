import random
from moead_framework.core.genetic_operator.abstract_operator import GeneticOperator


class BinaryMutation(GeneticOperator):
    """
    Binary Mutation operator.

    Require only one solution. Try to mutate each bit of the decision_vector with a predefined probability.
    """

    def __init__(self, solutions, mutation_probability=None):
        """
        Constructor of the Binary Mutation operator

        :param solutions: list<list<integer>> list of solution's representation (In algorithms, it is represented by the attribute :class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution.decision_vector` of the class :class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`)
        :param mutation_probability: {float} the probability (between 0 and 1) to mutate a bit in the decision_vector. The default value is the probability to mutate one bit of the decision_vector
        """
        super().__init__(solutions)
        proba = mutation_probability
        default_proba = 1 / (len(self.solutions[0]))
        self.mutation_probability = default_proba if proba is None else float(proba)

    def run(self):
        """
        Execute the genetic operator

        :return: {:class:`~moead_framework.solution.one_dimension_solution.OneDimensionSolution`} the offspring
        """

        self.number_of_solution_is_correct(n=1)

        solution = self.solutions[0][:]

        for i in range(len(solution)):
            probability = random.random()

            if probability < self.mutation_probability:
                solution[i] = abs(solution[i] - 1)

        return solution
