# MOEA/D Framework

![Python application](https://github.com/moead-framework/framework/workflows/Python%20application/badge.svg?branch=master)
![PyPI](https://img.shields.io/pypi/v/moead-framework)
![GitHub](https://img.shields.io/github/license/moead-framework/framework?style=flat)
![PyPI - Downloads](https://img.shields.io/pypi/dm/moead-framework)

This package is a modular framework for multi-objective evolutionary algorithms by decomposition. 
This framework is designed to help researchers to study and design their own MOEA/D variants.

The documentation is available here : [https://moead-framework.github.io/documentation/](https://moead-framework.github.io/documentation/html/index.html) and can be edited on this repository : [https://github.com/moead-framework/documentation](https://github.com/moead-framework/documentation).

# Installation instructions

Create a virtual environment with [conda](https://docs.conda.io/en/latest/miniconda.html) or [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)

The package is available in pypi, you can install it with :

    pip install moead-framework
    
# Exemple

    from moead_framework.aggregation.tchebycheff import Tchebycheff
    from moead_framework.algorithm.combinatorial.moead import Moead
    from moead_framework.problem.combinatorial.rmnk import Rmnk
    from moead_framework.tool.result import save_population
    
    
    ###############################
    #      Init the problem       #
    ###############################
    # The file is available here : https://github.com/moead-framework/data/blob/master/problem/RMNK/Instances/rmnk_0_2_100_1_0.dat
    # Others instances are available here : https://github.com/moead-framework/data/tree/master/problem/RMNK/Instances
    instance_file = "rmnk_0_2_100_1_0.dat"
    rmnk = Rmnk(instance_file=instance_file)
    
    
    ###############################
    #      Init the algorithm     #
    ###############################
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

## build : 

You can execute unit test with the following command in the git repository: 

    python3 -m unittest 


The package is build with a github action. If you want to create manually a new package : 

    python3 setup.py sdist bdist_wheel
 
    python3 -m twine upload dist/*

