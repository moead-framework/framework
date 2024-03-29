.. _components:

Other components
===========================================

.. note:: Not all available components are compatible with each other.
    Refer to each component's documentation for more details on required attributes.

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


Abstract
---------------------------------

.. autosummary::
   :nosignatures:
   :toctree: moead_framework

   moead_framework.core.genetic_operator.abstract_operator.GeneticOperator

Offspring generator
__________________________________________

The offspring generator is the component that manage all the process to generate new offspring by
using components **Parent Selector** and **Genetic operator** for example.

.. autosummary::
   :template: class_custom.rst
   :nosignatures:
   :toctree: moead_framework

   moead_framework.core.offspring_generator.offspring_generator.OffspringGeneratorGeneric
   moead_framework.core.offspring_generator.abstract_mating.OffspringGenerator


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
   moead_framework.core.parent_selector.abstract_parent_selector.ParentSelector

Mating Selector
__________________________________________

The mating selector is the component used to select the set of solutions where we can find parents solutions.

.. autosummary::
   :nosignatures:
   :toctree: moead_framework

   moead_framework.core.selector.closest_neighbors_selector.ClosestNeighborsSelector
   moead_framework.core.selector.delta_selector.DeltaSelector
   moead_framework.core.selector.abstract_selector.MatingPoolSelector


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
   moead_framework.core.sps_strategy.abstract_sps.SpsStrategy


Termination criteria
__________________________________________

The termination criteria is the component used to determine when the algorithm has to stop.

.. autosummary::
   :nosignatures:
   :toctree: moead_framework

   moead_framework.core.termination_criteria.max_evaluation.MaxEvaluation
   moead_framework.core.termination_criteria.abstract_termination_criteria.TerminationCriteria
