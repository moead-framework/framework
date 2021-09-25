"""
This complete example shows how to use a custom component as input to the MOEA/D algorithm.
"""
from example2.offspring_generator_local_search import OffspringGeneratorWithHillClimber
from moead_framework.aggregation import Tchebycheff
from moead_framework.algorithm.combinatorial import Moead
from moead_framework.problem.combinatorial import Rmnk


###############################
#    Initialize the problem   #
###############################
# The file is available here : https://github.com/moead-framework/data/blob/master/problem/RMNK/Instances/rmnk_0_2_100_1_0.dat
# Others instances are available here : https://github.com/moead-framework/data/tree/master/problem/RMNK/Instances
instance_file = "rmnk_0_2_100_1_0.dat"
rmnk = Rmnk(instance_file=instance_file)


###############################
#  Initialize the algorithm   #
###############################
number_of_weight = 10
number_of_weight_neighborhood = 20
number_of_evaluations = 10000
# The file is available here : https://github.com/moead-framework/data/blob/master/weights/SOBOL-2objs-10wei.ws
# Others weights files are available here : https://github.com/moead-framework/data/tree/master/weights
weight_file = "SOBOL-" + str(rmnk.number_of_objective) + "objs-" + str(number_of_weight) + "wei.ws"


###############################
#    Execute the algorithm    #
###############################
moead = Moead(problem=rmnk,
              max_evaluation=number_of_evaluations,
              number_of_weight_neighborhood=number_of_weight_neighborhood,
              weight_file=weight_file,
              aggregation_function=Tchebycheff,
              offspring_generator=OffspringGeneratorWithHillClimber,
              )

population = moead.run()
