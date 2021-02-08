

Tutorials
===========================================

.. _tuto-problem:
Implement your own problem
--------------------------------------
To make your problem compliant with the framework, your problem class have to extend the class :class:`moead_framework.problem.Problem` 
and also implement the 3 required functions : 

- the fitness function :code:`f(function_id, solution)` has 2 required parameters. The function must returns the objectif value of the solution 
  for the objective function_id in parameter.

  .. note:: For a better compatibility with components, problems should be converted in minimization problems.

.. code-block:: python
    
    def f(self, function_id, solution):
        ...
        return objective_value



- The function :code:`generate_solution(array, evaluate)` allows to generate a solution. A solution is an object OneDimensionSolution that contains the representation of the solution in the attribute solution and all fitness values in the F attribute. 
 
 .. note:: All components of the framework available in this version are only compatible with OneDimensionSolution. If you want manage new type of solutions, you have to adapt other components of the framework. 
 
 The function :code:`generate_solution(array, evaluate)` takes in parameter the representation of the function and the boolean :code:`evaluate` 
 that determine if the solution save the fitness, the default value must be "True".

.. code-block:: python
    
        def generate_solution(self, array, evaluate=True):
            x = OneDimensionSolution(array)

            for j in range(self.function_numbers):
                if evaluate:
                    x.F.append(self.f(j, x.solution))
                else:
                    x.F.append(None)

            return x
  

- The function :code:`generate_random_solution(evaluate)` generates a solution **randomly** in the same way than the previous function.

.. code-block:: python

    def generate_random_solution(self, evaluate=True):
        return self.generate_solution(array=np.random.randint(0, 2, self.object_number).tolist()[:], evaluate=evaluate)




Implement your own algorithm
--------------------------------------------------------------------

:ref:`All components<components>` are set with default values to implement the first version of **MOEA/D**. 
You can customize each :ref:`algorithms<components_algo>` of the framework with your own 
components that you can set in parameter of the algorithm contructor.

Example for :class:`moead_framework.algorithm.combinatorial.moead` :

.. code-block:: python

    moead = Moead(
              # Mandatory parameters
              problem=rmnk,
              max_evaluation = number_of_evaluations,
              number_of_objective=number_of_objective,
              number_of_weight=number_of_weight,
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
    
    

If you want manage the way to use all this :ref:`components<components>`, you have to create 
a new algorithm by extending an available algorithm. Examples are available in this repository : https://github.com/moead-framework/framework/tree/master/moead_framework/algorithm.

For example with the implementation of MOEA/D-DE :cite:`moead_de` in the class :class:`moead_framework.algorithm.combinatorial.moead_delta_nr` that extends **Moead** to rewrite the 
function update_solutions() and add two new parameters. 


Save data with the framework
--------------------------------------------------------------------

You can easily save a set of solutions by using the function :code:`save_population("population.txt", population)`. 
The function must be imported with : :code:`from moead_framework.tool.result import save_population`.


If you want save all non-dominated solutions (attribute :code:`self.ep` in the algorithm) every 10 evaluations, you can use the checkpoint parameter of the function :code:`algorithm.run()` :


.. code-block:: python

    moead = Moead(
              problem=rmnk,
              max_evaluation = number_of_evaluations,
              number_of_objective=number_of_objective,
              number_of_weight=number_of_weight,
              number_of_weight_neighborhood=number_of_weight_neighborhood,
              weight_file=weight_file,
              aggregation_function=Tchebycheff
              )

    def checkpt():
        if moead.current_eval % 10 ==0 :      
            filename = "non_dominated_solutions-eval" + str(moead.current_eval) + ".txt"
            save_population(file_name=filename, population=moead.ep)
    
    moead.run(checkpoint=checkpt)