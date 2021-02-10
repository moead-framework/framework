.. _components:

Main components
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

