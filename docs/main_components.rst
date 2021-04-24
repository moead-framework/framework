.. _components:

Main components
===========================================


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


.. note:: You can implement your own algorithm by following :ref:`this tutorial<tuto-algo>`.


Aggregation functions
__________________________________________

The aggregation function is used in MOEA/D to decompose the multi-objective problem into several mono-objective sub-problems.
The two main functions used are the Weighted Sum and the Tchebycheff function. In our framework, the aggregation function
is a required parameter of the algorithm.

.. autosummary::
   :template: class_custom.rst
   :nosignatures:
   :toctree: moead_framework

   moead_framework.aggregation.tchebycheff.Tchebycheff
   moead_framework.aggregation.weighted_sum.WeightedSum

