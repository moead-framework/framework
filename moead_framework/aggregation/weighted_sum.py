from .functions import AggregationFunction


class WeightedSum(AggregationFunction):
    """
    Weighted Sum aggregation function
    """
    def is_better(self, old_value, new_value):
        """
        Allow to compare 2 aggregations values for the weighted-sum function in a minimization context.

        :param old_value: {float} old aggregation value
        :param new_value: {float} new aggregation value
        :return: {boolean} True if new_value is better than old_value.
        """
        return new_value < old_value

    def run(self, solution, number_of_objective, weights, sub_problem, z):
        res = 0
        for i in range(number_of_objective):
            res += solution.F[i] * weights[sub_problem][i]
        return res
