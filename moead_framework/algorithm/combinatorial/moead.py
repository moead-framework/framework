from moead_framework.algorithm.abstract_moead import AbstractMoead
from moead_framework.core.genetic_operator.combinatorial.cross_mut import CrossoverAndMutation
from moead_framework.core.parent_selector.two_random_parent_selector import TwoRandomParentSelector
from moead_framework.tool.mop import get_non_dominated, is_duplicated


class Moead(AbstractMoead):

    def __init__(self, problem,
                 max_evaluation,
                 number_of_objective,
                 number_of_weight,
                 number_of_weight_neighborhood,
                 aggregation_function,
                 termination_criteria=None,
                 number_of_crossover_points=2,
                 mating_pool_selector=None,
                 genetic_operator=None,
                 parent_selector=None,
                 sps_strategy=None,
                 offspring_generator=None,
                 weight_file=None):

        self.current_eval = 1
        self.mating_pool = []

        super().__init__(problem,
                         max_evaluation,
                         number_of_objective,
                         number_of_weight,
                         number_of_weight_neighborhood,
                         termination_criteria=termination_criteria,
                         aggregation_function=aggregation_function,
                         genetic_operator=genetic_operator,
                         mating_pool_selector=mating_pool_selector,
                         parent_selector=parent_selector,
                         sps_strategy=sps_strategy,
                         offspring_generator=offspring_generator,
                         weight_file=weight_file)
        self.number_of_crossover_points = number_of_crossover_points

        if genetic_operator is None:
            self.genetic_operator = CrossoverAndMutation
        else:
            self.genetic_operator = genetic_operator

        if parent_selector is None:
            self.parent_selector = TwoRandomParentSelector(algorithm=self)
        else:
            self.parent_selector = parent_selector

    def run(self, checkpoint=None):

        while self.termination_criteria.test():

            # For each sub-problem i
            for i in self.get_sub_problems_to_visit():

                if checkpoint is not None:
                    checkpoint()

                self.update_current_sub_problem(sub_problem=i)
                self.mating_pool = self.mating_pool_selection(sub_problem=i)[:]
                y = self.generate_offspring(population=self.mating_pool)
                y = self.repair(solution=y)
                self.update_z(solution=y)
                self.update_solutions(solution=y, aggregation_function=self.aggregation_function, sub_problem=i)
                self.current_eval += 1

        return self.ep

    def update_solutions(self, solution, aggregation_function, sub_problem):

        for j in self.b[sub_problem]:
            y_score = aggregation_function.run(solution=solution,
                                               number_of_objective=self.number_of_objective,
                                               weights=self.weights,
                                               sub_problem=j,
                                               z=self.z)

            pop_j_score = aggregation_function.run(solution=self.population[j],
                                                   number_of_objective=self.number_of_objective,
                                                   weights=self.weights,
                                                   sub_problem=j,
                                                   z=self.z)

            if aggregation_function.is_better(pop_j_score, y_score):
                self.population[j] = solution

                if not is_duplicated(x=solution, population=self.ep, number_of_objective=self.number_of_objective):
                    self.ep.append(solution)
                    self.ep = get_non_dominated(self.ep)

