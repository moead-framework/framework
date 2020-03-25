from moead.aggregation.tchebycheff import Tchebycheff
from moead.algorithm.moead import Moead
from moead.problem.rmnk import Rmnk

from moead.tool.result import save_population


###############################
#      Init the problem       #
###############################
instance_file = "moead/data/RMNK/Instances/rmnk_0_2_100_1_0.dat"
rmnk = Rmnk(instance_file=instance_file)


###############################
#      Init the algorithm     #
###############################
number_of_objective = rmnk.function_numbers
number_of_weight = 10
number_of_weight_neighborhood = 20
number_of_crossover_points = 4
number_of_evaluations = 1000
weight_file = "moead/data/weights/SOBOL-" + str(number_of_objective) + "objs-" + str(number_of_weight) + "wei.ws"


###############################
#    Execute the algorithm    #
###############################
moead = Moead(problem=rmnk,
              max_evaluation = number_of_evaluations,
              number_of_objective=number_of_objective,
              number_of_weight=number_of_weight,
              number_of_weight_neighborhood=number_of_weight_neighborhood,
              number_of_crossover_points=number_of_crossover_points,
              weight_file=weight_file,
              )

population = moead.run(g=Tchebycheff())


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

