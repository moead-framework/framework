

Tutorials
===========================================

.. _tuto-problem:
Implement your own problem
--------------------------------------
To make your problem compliant with the framework, your problem class has to extend the class :class:`moead_framework.problem.Problem`
and implement the following 3 required functions :

- the fitness function :code:`f(function_id, solution)` has 2 required parameters. The function must return the objective value of the given ``solution``
  for the objective specified by ``function_id``.

.. note:: For compatibility with existing components, problems should be converted to minimization problems.

.. code-block:: python
    
    def f(self, function_id, solution):
        ...
        return objective_value



- The function :code:`generate_solution(array, evaluate)` generates a solution. A solution is a :class:`moead_framework.solution.one_dimensional_dolution.OneDimensionSolution` object that contains the representation of the solution in the ``solution`` attribute, and all fitness values in the ``F`` attribute.
 
.. note:: All components of the framework available in this version are only compatible with OneDimensionSolution. If you want to manage new types of solutions, you have to adapt other components of the framework.
 
The function :code:`generate_solution(array, evaluate)` takes as parameter ``array`` the representation of the solution and the boolean :code:`evaluate`
that determine if the solution object should save the fitness, the default value must be ``True``.

.. code-block:: python
    
        def generate_solution(self, array, evaluate=True):
            x = OneDimensionSolution(array)

            for j in range(self.function_numbers):
                if evaluate:
                    x.F.append(self.f(j, x.solution))
                else:
                    x.F.append(None)

            return x
  

- The function :code:`generate_random_solution(evaluate)` generates a solution **randomly** in the same way as the previous function.

.. code-block:: python

    def generate_random_solution(self, evaluate=True):
        return self.generate_solution(array=np.random.randint(0, 2, self.object_number).tolist()[:], evaluate=evaluate)



.. _tuto-algo:
Implement your own algorithm
--------------------------------------------------------------------

All components are set with default values to implement the first version of **MOEA/D**.
You can customize each algorithm in the framework with your own
components that you can set as parameter of the algorithm contructor.

Example for :class:`moead_framework.algorithm.combinatorial.moead` :

.. code-block:: python

    moead = Moead(
              # Mandatory parameters
              problem=rmnk,
              max_evaluation = number_of_evaluations,
              number_of_weight_neighborhood=number_of_weight_neighborhood,
              weight_file=weight_file,
              aggregation_function=Tchebycheff,
              # Optional parameters
              termination_criteria=MaxEvaluation,
              number_of_crossover_points=2,
              mutation_probability=1,
              mating_pool_selector=ClosestNeighborsSelector,
              genetic_operator=CrossoverAndMutation,
              parent_selector=TwoRandomParentSelector,
              sps_strategy=SpsAllSubproblems,
              offspring_generator=OffspringGeneratorGeneric
              )



If you want to manage the way to use all these components, you have to create
a new algorithm by extending an available algorithm. Examples are available in this repository : https://github.com/moead-framework/framework/tree/master/moead_framework/algorithm.

An example is the implementation of MOEA/D-DE :cite:`moead_de` in the class :class:`moead_framework.algorithm.combinatorial.moead_delta_nr` that extends **Moead** to rewrite the
function ``update_solutions()`` and adds two new parameters.


Manage the reproducibility of results
--------------------------------------------------------------------

Reproducibility of results is a major principle for scientific research.
The feature used here is not specific to the framework but
can be used for every python project that uses the `numpy` and built-in `random` modules.

Because the framework uses the `random` and `numpy` modules, you can be sure
to have the same results by running the same script several times if you
add the following instructions before initializing problems or algorithms:

.. code-block:: python

    import random
    import numpy

    seed = 0
    random.seed(seed)
    np.random.seed(seed)


You can find more information at the following links:

- https://docs.python.org/3/library/random.html
- https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html


Save data with the framework
--------------------------------------------------------------------

You can easily save a set of solutions by using the function :code:`save_population("population.txt", population)`. 
The function must be imported with : :code:`from moead_framework.tool.result import save_population`.


If you want to save all non-dominated solutions (attribute :code:`self.ep` in the algorithm) every e.g. 10 evaluations, you can use the checkpoint parameter of the function :code:`algorithm.run()` :


.. code-block:: python

    moead = Moead(
              problem=rmnk,
              max_evaluation = number_of_evaluations,
              number_of_weight_neighborhood=number_of_weight_neighborhood,
              weight_file=weight_file,
              aggregation_function=Tchebycheff
              )

    def checkpt():
        if moead.current_eval % 10 ==0 :      
            filename = "non_dominated_solutions-eval" + str(moead.current_eval) + ".txt"
            save_population(file_name=filename, population=moead.ep)
    
    moead.run(checkpoint=checkpt)


Extract and plot the Pareto front
--------------------------------------------------------------------

The method `run()` of each algorithm return a list of :class:`moead_framework.solution.one_dimension_solution.OneDimensionSolution`.

.. code-block:: python

    moead = Moead(
              problem=rmnk,
              max_evaluation = number_of_evaluations,
              number_of_weight_neighborhood=number_of_weight_neighborhood,
              weight_file=weight_file,
              aggregation_function=Tchebycheff
              )

    list_of_solution = moead.run(checkpoint=checkpt)


You can then extract the Pareto set and the Pareto front :

.. code-block:: python

    pareto_front = []
    pareto_set = []

    for solution_object in list_of_solution:
        pareto_front.append(solution_object.F)
        pareto_set.append(solution_object.solution)


If you want plot the Pareto front with matplotlib, you can do it with :

.. code-block:: python

    from matplotlib import pyplot as plt
    import numpy as np

    data = np.array(pareto_front)
    x, y = data.T
    plt.scatter(x,y)
    plt.show()
