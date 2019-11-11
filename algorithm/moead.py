from algorithm.abstract_moead import AbstractMoead
from tool.mop import get_non_dominated, is_duplicated


class Moead(AbstractMoead):

    def __init__(self, problem,
                 max_evaluation,
                 number_of_objective,
                 number_of_weight,
                 number_of_weight_neighborhood,
                 number_of_crossover_points=2,
                 genetic_selector=None,
                 genetic_operator=None,
                 genetic_mating=None,
                 weight_file=None):

        self.current_eval = 1

        super().__init__(problem,
                         max_evaluation,
                         number_of_objective,
                         number_of_weight,
                         number_of_weight_neighborhood,
                         number_of_crossover_points,
                         genetic_operator=genetic_operator,
                         genetic_selector=genetic_selector,
                         genetic_mating=genetic_mating,
                         weight_file=weight_file)

    def run(self, g, checkpoint=None):

        while self.current_eval < self.max_evaluation:

            # For each sub-problem i
            for i in self.sps_strategy():

                self.update_current_sub_problem(sub_problem=i)
                selected_population = self.selection(sub_problem=i)
                y = self.reproduction(population=selected_population)
                y = self.repair(solution=y)
                self.update_z(solution=y)
                self.update_solutions(solution=y, scal_function=g, sub_problem=i)
                self.current_eval += 1

        return self.ep

    def sps_strategy(self):
        return range(self.number_of_weight)

    def selection(self, sub_problem):
        return self.genetic_selector.select(sub_problem)

    def reproduction(self, population):
        return self.genetic_mating(algorithm_instance=self).run(population_indexes=population)

    def repair(self, solution):
        return solution
    
    def initial_population(self):
        p = []
        x_i = self.problem.generate_random_solution()

        if not is_duplicated(x=x_i, population=self.ep, number_of_objective=self.number_of_objective):
            self.ep.append(x_i)
            self.ep = get_non_dominated(self.ep, self.number_of_objective)

        for i in range(self.number_of_weight):
            p.append(x_i)

        return p

    def update_solutions(self, solution, scal_function, sub_problem):

        for j in self.b[sub_problem]:
            y_score = scal_function.run(solution=solution,
                                        number_of_objective=self.number_of_objective,
                                        weights=self.weights,
                                        sub_problem=j,
                                        z=self.z)

            pop_j_score = scal_function.run(solution=self.population[j],
                                            number_of_objective=self.number_of_objective,
                                            weights=self.weights,
                                            sub_problem=j,
                                            z=self.z)

            if scal_function.is_better(pop_j_score, y_score):
                self.population[j] = solution

                if not is_duplicated(x=solution, population=self.ep, number_of_objective=self.number_of_objective):
                    self.ep.append(solution)
                    self.ep = get_non_dominated(self.ep, self.number_of_objective)

