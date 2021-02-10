# MOEA/D Framework

[![status](https://joss.theoj.org/papers/a81ea21d0358e013000b0b3b926bd4ba/status.svg)](https://joss.theoj.org/papers/a81ea21d0358e013000b0b3b926bd4ba)
[![Python application](https://github.com/moead-framework/framework/workflows/Python%20application/badge.svg?branch=master)](https://github.com/moead-framework/framework/actions?query=workflow%3A%22Python+application%22)
[![codecov](https://codecov.io/gh/moead-framework/framework/branch/master/graph/badge.svg?token=J7MAU5E6BB)](https://codecov.io/gh/moead-framework/framework)
[![PyPI](https://img.shields.io/pypi/v/moead-framework)](https://pypi.org/project/moead-framework/)
[![GitHub](https://img.shields.io/github/license/moead-framework/framework?style=flat)](https://github.com/moead-framework/framework/blob/master/LICENCE)

This python package *moead-framework* is a modular framework for multi-objective evolutionary algorithms by decomposition. 
The goal  is to provide a modular framework for scientists and researchers interested in 
experimenting with MOEA/D and its numerous variants.

The documentation is available here: [https://moead-framework.github.io/framework/](https://moead-framework.github.io/framework/html/index.html) and can be edited in the folder docs of this repository.

# Installation instructions

Create a virtual environment with [conda](https://docs.conda.io/en/latest/miniconda.html) or [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)

The package is available in pypi with a linux environment for python 3.6, 3.7, 3.8 and 3.9, you can install it with:

    pip install moead-framework
    
# Example

    from moead_framework.aggregation import Tchebycheff
    from moead_framework.algorithm.combinatorial import Moead
    from moead_framework.problem.combinatorial import Rmnk
    from moead_framework.tool.result import save_population
    
    
    ###############################
    #   Initialize the problem    #
    ###############################
    # The file is available here : https://github.com/moead-framework/data/blob/master/problem/RMNK/Instances/rmnk_0_2_100_1_0.dat
    # Others instances are available here : https://github.com/moead-framework/data/tree/master/problem/RMNK/Instances
    instance_file = "rmnk_0_2_100_1_0.dat"
    rmnk = Rmnk(instance_file=instance_file)
    
    
    #####################################
    #      Initialize the algorithm     #
    #####################################
    number_of_objective = rmnk.function_numbers
    number_of_weight = 10
    number_of_weight_neighborhood = 20
    number_of_evaluations = 1000
    # The file is available here : https://github.com/moead-framework/data/blob/master/weights/SOBOL-2objs-10wei.ws
    # Others weights files are available here : https://github.com/moead-framework/data/tree/master/weights
    weight_file = "SOBOL-" + str(number_of_objective) + "objs-" + str(number_of_weight) + "wei.ws"
    
    
    ###############################
    #    Execute the algorithm    #
    ###############################
    moead = Moead(problem=rmnk,
                  max_evaluation=number_of_evaluations,
                  number_of_objective=number_of_objective,
                  number_of_weight=number_of_weight,
                  number_of_weight_neighborhood=number_of_weight_neighborhood,
                  weight_file=weight_file,
                  aggregation_function=Tchebycheff,
                  )
    
    population = moead.run()
    
    
    ###############################
    #       Save the result       #
    ###############################
    save_file = "moead-rmnk" + str(number_of_objective) \
                + "-N" + str(number_of_weight) \
                + "-T" + str(number_of_weight_neighborhood) \
                + "-CP" + str(number_of_crossover_points) \
                + "-iter" + str(number_of_evaluations) \
                + ".txt"
    
    save_population(save_file, population)



# For developers 

## build: 

You can execute unit test with the following command in the git repository: 

    python3 -m unittest 


The package is build with a github action. If you want to create manually a new package: 

    python3 setup.py sdist bdist_wheel
 
    python3 -m twine upload dist/*

