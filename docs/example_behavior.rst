
Update the behavior of MOEA/D without using inner components
--------------------------------------

In some situations, the framework components may not allow you to implement all your ideas.
In this case, you can directly alter the behavior of the algorithms as we will see in this example.

In this example, we want to shuffle all weight vectors at the end of each generation.
To do this, we need to extend the algorithm class and more precisely
the ```run``` method to add one line : ``random.shuffle(self.weights)``.

You can rewrite all methods available in algorithms : https://moead-framework.github.io/framework/html/moead_framework/moead_framework.algorithm.abstract_moead.AbstractMoead.html#moead-framework-algorithm-abstract-moead-abstractmoead

.. literalinclude:: examples/example3/moead_example.py
  :language: python

