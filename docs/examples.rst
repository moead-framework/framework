
Examples
===========================================

Optimise mnk-landscapes with MOEA/D
--------------------------------------

The example requires two files :

- ```instance_file``` is required by the problem. The file is available in the framework in "moead_framework/test/data/instances/" or can be downloaded from https://github.com/moead-framework/data/tree/master/problem/RMNK/Instances

- ```weight_file``` is required by the algorithm. The file is available in the framework in "moead_framework/test/data/weights/" or can be downloaded from https://github.com/moead-framework/data/tree/master/weights


.. literalinclude:: examples/example_rmnk_moead.py
  :language: python

