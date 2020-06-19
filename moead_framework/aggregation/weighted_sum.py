from .functions import AggregationFunction


class WeightedSum(AggregationFunction):

    def is_better(self, old_value, new_value):
        """In minimization context only"""
        return new_value < old_value

    def run(self, solution, number_of_objective, weights, sub_problem, z):
        res = 0
        for i in range(number_of_objective):
            res += solution.F[i] * weights[sub_problem][i]
        return res


# def weighted_sum(**args):
#     if not (("solution" in args)
#             & ("number_of_objective" in args)
#             & ("weights" in args)
#             & ("sub_problem" in args)):
#         raise KeyError("Parameters required : 'solution', 'number_of_objective', 'weights', 'sub_problem'")
#
#     solution = args["solution"]
#     number_of_objective = args["number_of_objective"]
#     weights = args["weights"]
#     sub_problem = args["sub_problem"]
#     res = 0
#     for i in range(number_of_objective):
#         res += solution.F[i] * weights[sub_problem][i]
#     return res
