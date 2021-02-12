from .functions import AggregationFunction


class Tchebycheff(AggregationFunction):
    """
    Tchebycheff aggregation function.

    Minimize the maximal distance \|f_i(x) - z_i(x)\| * w_i
    """

    def is_better(self, old_value, new_value):
        """
        Allow to compare 2 aggregations values for the tchebycheff function in a minimization context.

        :param old_value: {float} old aggregation value
        :param new_value: {float} new aggregation value
        :return: {boolean} True if new_value is better than old_value.
        """
        return new_value < old_value

    def run(self, solution, number_of_objective, weights, sub_problem, z):
        max_distance = 0

        for i in range(number_of_objective):
            current_score = abs(solution.F[i] - z[i]) * weights[sub_problem][i]

            max_distance = max(max_distance, current_score)

        return max_distance
