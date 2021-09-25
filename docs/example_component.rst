
Create your own variant of MOEA/D with the modularity of the framework
--------------------------------------

The moead-framework provides many components to allow you to create your own variant of the MOEA/D algorithm.
The documentation of all components is available here : https://moead-framework.github.io/framework/html/api.html.

In this example, we want to use a local search algorithm (hill climber first improvement) after the generation of each new solution (offspring).
To do this, we implement a new offspring generator that will extend the component ```OffspringGeneratorGeneric``` that is used by
default in MOEA/D.


.. literalinclude:: examples/example2/offspring_generator_local_search.py
  :language: python

The component is then set as a parameter to the algorithm's constructor.

.. literalinclude:: examples/example2/example_component.py
  :language: python