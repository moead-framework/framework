import random
from moead_framework.algorithm.combinatorial import Moead


class MoeadExample(Moead):

    def run(self, checkpoint=None):

        while self.termination_criteria.test():

            # For each sub-problem i
            for i in self.get_sub_problems_to_visit():

                if checkpoint is not None:
                    checkpoint(self)

                self.optimize_sub_problem(sub_problem_index=i)
                # shuffle all weights
                random.shuffle(self.weights)

        return self.ep
