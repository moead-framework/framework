.. _components:

Components of MOEA/D framework
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

You can find examples of file instances for combinatorial problems
in this repository https://github.com/moead-framework/data/tree/master/problem.

.. note:: You can implement your own problem by following :ref:`this tutoriel<tuto-problem>`.


Solution
__________________________________________

.. autosummary::
   :nosignatures:
   :toctree: moead_framework

   moead_framework.solution.one_dimension_solution.OneDimensionSolution


Algorithms
__________________________________________

These algorithms are implemented on the basis of the original papers (:cite:`moead`, :cite:`moead_de`, :cite:`moead_dra`, :cite:`gpruvost_evocop2020`).

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


.. note:: You can implement your own algorithm by following :ref:`this tutoriel<tuto-algo>`.


Aggregation functions
__________________________________________

The aggregation function is used in MOEA/D to decompose the multi-objective problem into several mono-objective sub-problems.
The two main functions used are the Weighted Sum and the Tchebycheff function. In our framework, the aggregation function
is a required parameter of the algorithm.

.. autosummary::
   :nosignatures:
   :toctree: moead_framework

   moead_framework.aggregation.tchebycheff.Tchebycheff
   moead_framework.aggregation.weighted_sum.WeightedSum


Genetic operators
__________________________________________

A genetic operator is a component used in genetic algorithms to generate offspring by
using characteristics of parents solutions. In the framework, these operators are used in the component **offspring_generator**.


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

The offspring generator is the component that manage all the process to generate new offspring by
using components **Parent Selector** and **Genetic operator** for example.

.. autosummary::
   :nosignatures:
   :toctree: moead_framework

   moead_framework.core.offspring_generator.offspring_generator.OffspringGeneratorGeneric


Parent Selector
__________________________________________

The parent selector is the component used to select solutions in the neighborhood before to use genetic
operators to generate new offspring.

.. autosummary::
   :nosignatures:
   :toctree: moead_framework

   moead_framework.core.parent_selector.one_random_and_current_parent_selector.OneRandomAndCurrentParentSelector
   moead_framework.core.parent_selector.two_random_and_current_parent_selector.TwoRandomAndCurrentParentSelector
   moead_framework.core.parent_selector.two_random_parent_selector.TwoRandomParentSelector


Mating Selector
__________________________________________

The mating selector is the component used to select the set of solutions where we can find parents solutions.

.. autosummary::
   :nosignatures:
   :toctree: moead_framework

   moead_framework.core.selector.closest_neighbors_selector.ClosestNeighborsSelector
   moead_framework.core.selector.delta_selector.DeltaSelector


Sub-problem selection strategy
__________________________________________

The SPS Strategy :cite:`gpruvost_evocop2020` is the component used to select sub-problems
(or solutions of the population) that will be visited during the next
generation of MOEA/D.

.. autosummary::
   :nosignatures:
   :toctree: moead_framework

   moead_framework.core.sps_strategy.sps_all.SpsAllSubproblems
   moead_framework.core.sps_strategy.sps_dra.SpsDra
   moead_framework.core.sps_strategy.sps_random_and_boundaries.SpsRandomAndBoundaries


Termination criteria
__________________________________________

The termination criteria is the component used to determine when the algorithm has to stop.

.. autosummary::
   :nosignatures:
   :toctree: moead_framework

   moead_framework.core.termination_criteria.max_evaluation.MaxEvaluation
