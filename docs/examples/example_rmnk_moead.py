from moead_framework.aggregation import Tchebycheff
from moead_framework.algorithm.combinatorial import Moead
from moead_framework.problem.combinatorial import Rmnk
from moead_framework.tool.result import save_population


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

