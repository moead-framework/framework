from moead_framework.algorithm.abstract_moead import AbstractMoead
from moead_framework.core.genetic_operator.combinatorial.cross_mut import CrossoverAndMutation
from moead_framework.core.parent_selector.two_random_parent_selector import TwoRandomParentSelector


class Moead(AbstractMoead):
    """
    Implementation of MOEA/D for combinatorial problems.
    """

    def __init__(self, problem,
                 max_evaluation,
                 number_of_objective,
                 number_of_weight,
                 number_of_weight_neighborhood,
                 aggregation_function,
                 weight_file,
                 termination_criteria=None,
                 number_of_crossover_points=2,
                 mutation_probability=1,
                 mating_pool_selector=None,
                 genetic_operator=None,
                 parent_selector=None,
                 sps_strategy=None,
                 offspring_generator=None,
                 ):
        """
        Constructor of the algorithm.

        :param problem: {:class:`~moead_framework.problem.Problem`} problem to optimize
        :param max_evaluation: {integer} maximum number of evaluation
        :param number_of_objective: {integer} number of objective in the problem
        :param number_of_weight: {integer} number of weight vector used to decompose the problem
        :param number_of_weight_neighborhood: {integer} size of the neighborhood
        :param aggregation_function: {:class:`~moead_framework.aggregation.functions.AggregationFunction`}
        :param termination_criteria: Optional -- {:class:`~moead_framework.core.termination_criteria.abstract_termination_criteria.TerminationCriteria`} The default component is {:class:`~moead_framework.core.termination_criteria.max_evaluation.MaxEvaluation`}
        :param genetic_operator: Optional -- {:class:`~moead_framework.core.genetic_operator.abstract_operator.GeneticOperator`} The default operator is :class:`~moead_framework.core.genetic_operator.combinatorial.cross_mut.CrossoverAndMutation`
        :param parent_selector: Optional -- {:class:`~moead_framework.core.parent_selector.abstract_parent_selector.ParentSelector`} The default operator is :class:`~moead_framework.core.parent_selector.two_random_parent_selector.TwoRandomParentSelector`
        :param mating_pool_selector: Optional -- {:class:`~moead_framework.core.selector.abstract_selector.MatingPoolSelector`} The default selector is {:class:`~moead_framework.core.selector.closest_neighbors_selector.ClosestNeighborsSelector`}
        :param sps_strategy: Optional -- {:class:`~moead_framework.core.sps_strategy.abstract_sps.SpsStrategy`} The default strategy is {:class:`~moead_framework.core.sps_strategy.sps_all.SpsAllSubproblems`}
        :param offspring_generator: Optional -- {:class:`~moead_framework.core.offspring_generator.abstract_mating.OffspringGenerator`} The default generator is {:class:`~moead_framework.core.offspring_generator.offspring_generator.OffspringGeneratorGeneric`}
        :param weight_file: todo need refactoring
        """

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
        self.mutation_probability = mutation_probability

        if genetic_operator is None:
            self.genetic_operator = CrossoverAndMutation
        else:
            self.genetic_operator = genetic_operator

        if parent_selector is None:
            self.parent_selector = TwoRandomParentSelector(algorithm=self)
        else:
            self.parent_selector = parent_selector
