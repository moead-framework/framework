
API
===========================================

Problems
__________________________________________

.. autosummary::
   :nosignatures:
   :toctree: moead_framework

   moead_framework.problem.combinatorial.rmnk.Rmnk
   moead_framework.problem.combinatorial.mubqp.Mubqp
   moead_framework.problem.combinatorial.knapsack.KnapsackProblem
   moead_framework.problem.numerical.zdt.Zdt1


Solution
__________________________________________

.. autosummary::
   :nosignatures:
   :toctree: moead_framework

   moead_framework.solution.one_dimension_solution.OneDimensionSolution


Algorithms
__________________________________________

For combinatorial problems
---------------------------------

.. autosummary::
   :nosignatures:
   :toctree: moead_framework

   moead_framework.algorithm.combinatorial.moead.Moead
   moead_framework.algorithm.combinatorial.moead_delta_nr.MoeadDeltaNr
   moead_framework.algorithm.combinatorial.moead_dra.MoeadDRA
   moead_framework.algorithm.combinatorial.moead_sps_random.MoeadSPSRandom

For numerical problems
---------------------------------

.. autosummary::
   :nosignatures:
   :toctree: moead_framework

   moead_framework.algorithm.numerical.moead.Moead


Aggregation functions
__________________________________________

.. autosummary::
   :nosignatures:
   :toctree: moead_framework

   moead_framework.aggregation.tchebycheff.Tchebycheff
   moead_framework.aggregation.weighted_sum.WeightedSum


Genetic operators
__________________________________________

For combinatorial problems
---------------------------------

.. autosummary::
   :nosignatures:
   :toctree: moead_framework

   moead_framework.core.genetic_operator.combinatorial.mutation.BinaryMutation
   moead_framework.core.genetic_operator.combinatorial.crossover.Crossover
   moead_framework.core.genetic_operator.combinatorial.cross_mut.CrossoverAndMutation


For numerical problems
---------------------------------

.. autosummary::
   :nosignatures:
   :toctree: moead_framework

   moead_framework.core.genetic_operator.numerical.differential_evolution_crossover.DifferentialEvolutionCrossover
   moead_framework.core.genetic_operator.numerical.polynomial_mutation.PolynomialMutation
   moead_framework.core.genetic_operator.numerical.moead_de_operators.MoeadDeOperators


Offspring generator
__________________________________________

.. autosummary::
   :nosignatures:
   :toctree: moead_framework

   moead_framework.core.offspring_generator.offspring_generator.OffspringGeneratorGeneric


Parent Selector
__________________________________________

.. autosummary::
   :nosignatures:
   :toctree: moead_framework

   moead_framework.core.parent_selector.one_random_and_current_parent_selector.OneRandomAndCurrentParentSelector
   moead_framework.core.parent_selector.two_random_and_current_parent_selector.TwoRandomAndCurrentParentSelector
   moead_framework.core.parent_selector.two_random_parent_selector.TwoRandomParentSelector


Mating Selector
__________________________________________

.. autosummary::
   :nosignatures:
   :toctree: moead_framework

   moead_framework.core.selector.closest_neighbors_selector.ClosestNeighborsSelector
   moead_framework.core.selector.delta_selector.DeltaSelector


Sub-problem selection strategy
__________________________________________

.. autosummary::
   :nosignatures:
   :toctree: moead_framework

   moead_framework.core.sps_strategy.sps_all.SpsAllSubproblems
   moead_framework.core.sps_strategy.sps_dra.SpsDra
   moead_framework.core.sps_strategy.sps_random_and_boundaries.SpsRandomAndBoundaries


Termination criteria
__________________________________________

.. autosummary::
   :nosignatures:
   :toctree: moead_framework

   moead_framework.core.termination_criteria.max_evaluation.MaxEvaluation
