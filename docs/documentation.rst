.. _components:
Components of MOEA/D framework
===========================================


Problems 
--------------------------------------

========================================= ======================================================= ===================================================================
Common Name                               Name in the framework                                   Parameters
========================================= ======================================================= ===================================================================
rho MNK-Landscapes :cite:`rmnk`           :class:`moead_framework.problem.combinatorial.rmnk`     :code:`instance_file` : path of the instance file
MUBQP :cite:`mubqp`                       :class:`moead_framework.problem.combinatorial.mubqp`    :code:`instance_file` : path of the instance file
Multi-objective Knapsack :cite:`mokp`     :class:`moead_framework.problem.combinatorial.knapsack` :code:`objective_number` : number of objective, :code:`instance_file` : path of the instance file
Zdt1 :cite:`zdt`                           :class:`moead_framework.problem.numerical.zdt`          :code:`size` : size of solutions
========================================= ======================================================= ===================================================================
 
Four benchmark problems are available in the framework. You can find file instances for combinatorial problems
in this repository https://github.com/moead-framework/data/tree/master/problem. 

.. note:: You can implement your own problem by following :ref:`this tutoriel<tuto-problem>`.

Three functions are available in a problem object: 

============================================================ ===================================================================
Function                                                     Comments
============================================================ ===================================================================
:class:`problem.generate_random_solution(evaluate)`          Generate a random solution. The parameter :code:`evaluate` is a boolean to specify if the solution have to be evaluated. The default value is :code:`True`.
:class:`problem.generate_solution(x, evaluate)`              Convert the list :code:`x` to a Solution object. The parameter :code:`evaluate` is a boolean to specify if the solution have to be evaluated. The default value is :code:`True`.
:class:`problem.f(i, solution)`                              Return the fitness value of the :code:`solution` object for the function :code:`i`.
============================================================ ===================================================================

A solution is a :code:`OneDimensionSolution` object. This object save the array in the attribute 
:code:`OneDimensionSolution.solution`, the fitness is saved in the array  :code:`OneDimensionSolution.F` if the  
parameter :code:`evaluate` is set to True.

Example with the problem rho MNK-Landscapes:

.. code-block:: python

    In [1]: from moead_framework.problem.combinatorial import Rmnk

    # the file is available here: https://github.com/moead-framework/data/blob/master/problem/RMNK/Instances/rmnk_0_2_20_1_0.dat
    # rmnk instance with parameters rho=0, m=2, n=20, k=1 and a seed of 0
    In [2]: file_rmnk = "rmnk_0_2_20_1_0.dat"  
    In [3]: problem = Rmnk(instance_file=file_rmnk) 

    # Generate a random solution
    In [4]: solution = problem.generate_random_solution()

    # Generate a solution with predefined values
    In [5]: solution = problem.generate_solution([0,1,1,1,0,1,0,0,1,0])

    # Get objective value of the solution
    In [6]: array_of_fitness = solution.F
    In [7]: f0 = solution.F[0]
    In [8]: f1 = solution.F[1]


.. _components_algo:
Algorithms
--------------------------------------

====================================================== ================================================================== ===================================================================
Common Name                                             Name in the framework                                              Comments
====================================================== ================================================================== ===================================================================
Original MOEA/D (combinatorial) :cite:`moead`           :class:`moead_framework.algorithm.combinatorial.moead`             The original algorithm for combinatorial optimization
Original MOEA/D (numerical) :cite:`moead`               :class:`moead_framework.algorithm.numerical.moead`                 The original algorithm for numerical optimization
MOEA/D with parameters delta / nr :cite:`moead_de`      :class:`moead_framework.algorithm.combinatorial.moead_delta_nr`    Variant with parameters delta & nr of MOEA/D-DE
MOEA/D-DRA :cite:`moead_dra`                            :class:`moead_framework.algorithm.combinatorial.moead_dra`         Variant with a dynamic ressource allocation
====================================================== ================================================================== ===================================================================

Each algorithm can be executed with the :code:`run()` function. This function returns all non dominated solutions found by the 
algorithm. Example: 

.. code-block:: python
    
    moead = Moead(problem=rmnk,
              max_evaluation = number_of_evaluations,
              number_of_objective=number_of_objective,
              number_of_weight=number_of_weight,
              number_of_weight_neighborhood=number_of_weight_neighborhood,
              weight_file=weight_file,
              aggregation_function=Tchebycheff,
              )

    non_dominated_solutions = moead.run()

.. note:: If you want know more about all algorithms already available in the framework, you can find their implementation in https://github.com/moead-framework/framework/tree/master/moead_framework/algorithm.


Weight vectors 
--------------------------------------
For the decomposition of the multi-objective problems, we need weight vectors. 
These weights are initialized by using a text file in the algorithm contructor with the parameter :code:`weight_file` and the parameter :code:`number_of_weight`.
We propose some examples of weight files in this repository: https://github.com/moead-framework/data/tree/master/weights.


Aggregation function
--------------------------------------

The aggregation function is set as the parameter :code:`aggregation_function` in the algorithm contructor.

========================================= ========================================= 
Common Name                               Name in the framework                    
========================================= ========================================= 
Weighted Sum                              :class:`moead_framework.aggregation.weighted_sum`   
Tchebycheff                               :class:`moead_framework.aggregation.tchebycheff`    
========================================= ========================================= 

The aggregation function is used in MOEA/D to decompose the multi-objective problem into several mono-objective sub-problems. 
The two main functions used are the Weighted Sum and the Tchebycheff function. In our framework, the aggregation function
is a required parameter of the algorithm. It is represented in the framework by a class with two methods : 

.. code-block:: python

    class AggregationFunction:

        @abstractmethod
        def run(self, solution, number_of_objective, weights, sub_problem, z):
            """
            :param solution:
            :param number_of_objective:
            :param weights: array of weight vectors
            :param sub_problem: index of the sub-problem currently visited
            :param z: array of dimension 'number_of_objective', it is the reference point Z*
            :return: the aggregation value of the solution for the weight weights[sub-problem]
            """
            pass

        @abstractmethod
        def is_better(self, old_value, new_value):
            """
            :param old_value:
            :param new_value:
            :return: True if new_value (computed by run()) is better than old_value.
            The test depends of the aggregation function and of the context (minimization or maximization).
            """
            pass


Parent Selector
--------------------------------------

The parent selector is set as the parameter :code:`parent_selector` in the algorithm contructor.

The parent selector is the component used to select solutions in the neighborhood before to use genetic 
operators to generate new offspring. The parent selector is an optional 
parameter of the algorithm, a default operator is used if the parameter is not set (two random solutions).

========================================= ========================================= 
Common Name                               Name in the framework                    
========================================= ========================================= 
Two random solutions                      :class:`moead_framework.core.parent_selector.two_random_parent_selector`    
One random and current solution           :class:`moead_framework.core.parent_selector.one_random_and_current_parent_selector`    
Two random and current solution           :class:`moead_framework.core.parent_selector.two_random_and_current_parent_selector`    
========================================= ========================================= 

The parent selector is executed with the function select, this function takes in parameter a set of index that represents
solutions in the population, and more precisely, in the neighborhood. The select function returns solutions that will 
be used to generate new offspring with the genetic operator.


.. code-block:: python

    class ParentSelector:

        def __init__(self, algorithm):
            self.algorithm = algorithm

        @abstractmethod
        def select(self, indexes):
            pass



Genetic operator
--------------------------------------

The genetic operator is set as the parameter :code:`genetic_operator` in the algorithm contructor.

A genetic operator is a component used in genetic algorithms to generate offspring by 
using characteristics of parents solutions. In the framework, these operators are used in the component **offspring_generator**.
The genetic operator is an optional parameter of the algorithm, a default operator (crossover) is used if the parameter is not set.

.. note:: If you call the genetic operator manually, pay attention to the potential additional parameters available in the table below, otherwise algorithms manage them automatically.


========================================= ============================================================================================= ======================================================================================
Common Name                               Name in the framework                                                                         additional parameters in the constructor
========================================= ============================================================================================= ======================================================================================
Multi-point combinatorial crossover       :class:`moead_framework.core.genetic_operator.combinatorial.crossover`                        :code:`crossover_points` : number of crossover points
Binary mutation                           :class:`moead_framework.core.genetic_operator.combinatorial.mutation`                         :code:`mutation_probability` : the mutation rate is :code:`mutation_probability / n`
Differential Evolution Crossover          :class:`moead_framework.core.genetic_operator.numerical.differential_evolution_crossover`     /
Polynomial mutation                       :class:`moead_framework.core.genetic_operator.numerical.polynomial_mutation`                  /
========================================= ============================================================================================= ======================================================================================

It is represented in the framework by a class with two methods: 

.. code-block:: python

    class GeneticOperator:

        @abstractmethod
        def __init__(self, solutions, **kwargs):        
        """
        take in parameter parent solutions required by the operator and potential additional parameters
        """
            self.solutions = solutions
        

        @abstractmethod
        def run(self):
        """
        :return: the new offspring generated by the operator with the parent solutions
        """
            pass


Offspring Generator
--------------------------------------

The offspring generator is set as the parameter :code:`offspring_generator` in the algorithm contructor.

The offspring generator is the component that manage all the process to generate new offspring by 
using components **Parent Selector** and **Genetic operator**. By default, this component is fixed because 
it is generic for almost all MOEA/D variants when we need to generate one offspring. This component can be updated 
in parameter of the MOEAD class if you want to use new components to generate offspring such as surrogates models for example.

.. code-block:: python

    class OffspringGeneratorGeneric(OffspringGenerator):

        def run(self, population_indexes):

            parents = self.algorithm.parent_selector.select(indexes=population_indexes)

            parents_solutions = []
            for s in parents:
                parents_solutions.append(s.solution)

            if hasattr(self.algorithm, 'number_of_crossover_points'):
                crossover_point = self.algorithm.number_of_crossover_points
            else:
                crossover_point = None

            if hasattr(self.algorithm, 'mutation_probability'):
                mutation_probability = self.algorithm.mutation_probability
            else:
                mutation_probability = None

            y_sol = self.algorithm.genetic_operator(solutions=parents_solutions,
                                                    crossover_points=crossover_point,
                                                    mutation_probability=mutation_probability
                                                    ).run()

            return self.algorithm.problem.generate_solution(array=y_sol)



Termination criteria
--------------------------------------

The termination criteria is set as the parameter :code:`termination_criteria` in the algorithm contructor.

The termination criteria is the component used to determine when the algorithm ends. We implement in this framework
a default criteria based on a maximum number of evaluation (a parameter of the algorithm) but we allow you to define new critera.
The termination criteria is an optional parameter of the algorithm.

========================================= ========================================= 
Common Name                               Name in the framework                    
========================================= ========================================= 
Maximum number of evaluation              :class:`moead_framework.core.termination_criteria.max_evaluation`    
========================================= ========================================= 


SPS (Sub-Problem Selection) Strategy
--------------------------------------

The sps strategy is set as the parameter :code:`sps_strategy` in the algorithm contructor.

The SPS Strategy :cite:`gpruvost_evocop2020` is the component used to select sub-problems (or solutions of the population) that will be visited during the next 
generation of MOEA/D. The default SPS is the strategy of the classic MOEA/D where all
sub-problems are visited during one generation.

========================================================== ========================================= 
Common Name                                                Name in the framework                    
========================================================== ========================================= 
SPS that iterate over all sub-problems                     :class:`moead_framework.core.sps_strategy.sps_all`    
SPS Strategy used in MOEA/D-DRA                            :class:`moead_framework.core.sps_strategy.sps_dra`    
SPS Strategy to select random and boundaries sub-problems  :class:`moead_framework.core.sps_strategy.sps_random_and_boundaries.py`    
========================================================== ========================================= 

