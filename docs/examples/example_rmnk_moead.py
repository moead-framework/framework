"""
This full example shows how to optimize the rmnk problem with the MOEA/D algorithm implemented in the framework.
You will see how to initialize the optimization problem and the algorithm, how to run the algorithm and finally how to
interpret the results of the algorithm.
"""
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
number_of_weight = 10
number_of_weight_neighborhood = 20
number_of_evaluations = 1000
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
              )

population = moead.run()


###############################
#       Save the result       #
###############################
save_file = "moead-rmnk" + str(rmnk.number_of_objective) \
            + "-N" + str(number_of_weight) \
            + "-T" + str(number_of_weight_neighborhood) \
            + "-iter" + str(number_of_evaluations) \
            + ".txt"

save_population(save_file, population)


###############################
#    Extract the Pareto set   #
#     and the Pareto front    #
###############################
pareto_front = []
pareto_set = []

for solution_object in population:
    pareto_front.append(solution_object.F)
    pareto_set.append(solution_object.decision_vector)
