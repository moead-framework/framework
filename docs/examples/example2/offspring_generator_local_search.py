"""
The `OffspringGeneratorWithHillClimber` component is a custom `OffspringGenerator`used as an example
to show the modularity of the framework.
"""
import numpy as np
from moead_framework.core.offspring_generator import OffspringGeneratorGeneric

class OffspringGeneratorWithHillClimber(OffspringGeneratorGeneric):
    """
    Generate a new offspring by using the component OffspringGeneratorGeneric
    followed by a local search algorithm (Hill-climber First Improvement)
    """

    def run(self, population_indexes):
        candidate_solution = super().run(population_indexes)
        candidate_solution_after_localsearch = self.hill_climber_first_improvement(first_solution=candidate_solution)

        return self.algorithm.problem.evaluate(x=candidate_solution_after_localsearch)

    def hill_climber_first_improvement(self, first_solution):
        decision_vector_best_solution = first_solution.decision_vector
        best_agg_value = self.algorithm.aggregation_function.run(solution=self.algorithm.problem.evaluate(x=first_solution),
                                                                 number_of_objective=len(first_solution.F),
                                                                 weights=self.algorithm.weights,
                                                                 sub_problem=self.algorithm.current_sub_problem,
                                                                 z=self.algorithm.z)
        stuck_by_local_optima = False

        while not stuck_by_local_optima:
            for i in range(len(decision_vector_best_solution)):
                neighbor = np.copy(decision_vector_best_solution)
                neighbor[i] = abs(neighbor[i] - 1)
                self.algorithm.current_eval += 1

                neighbor_agg_value = self.algorithm.aggregation_function.run(solution=self.algorithm.problem.evaluate(x=neighbor),
                                                                             number_of_objective=len(first_solution.F),
                                                                             weights=self.algorithm.weights,
                                                                             sub_problem=self.algorithm.current_sub_problem,
                                                                             z=self.algorithm.z)

                if neighbor_agg_value < best_agg_value:  # when we minimize the aggregation function
                    best_agg_value = neighbor_agg_value
                    decision_vector_best_solution = neighbor
                else:
                    stuck_by_local_optima = True

        return decision_vector_best_solution
