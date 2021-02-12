import random

from moead_framework.core.sps_strategy.abstract_sps import SpsStrategy


class SpsDra(SpsStrategy):
    """
    The strategy used in MOEA/D-DRA.

    Q. Zhang, W. Liu and H. Li,
    "The performance of a new version of MOEA/D on CEC09 unconstrained MOP test instances"
    2009 IEEE Congress on Evolutionary Computation
    Trondheim, 2009, pp. 203-208
    doi: 10.1109/CEC.2009.4982949.
    """
    def get_sub_problems(self):
        """
        Select at first the indexes of the sub problems whose objectives are MOP
        individual objectives fi (i.e. boundaries sub-problems)
        and add sub-problems with a 10-tournament

        :return: {list<integer>} indexes of sub-problems
        """
        selection = []

        for w in range(self.algorithm.number_of_weight):
            count_zero = 0
            for o in self.algorithm.weights[w]:
                if o == 0:
                    count_zero += 1

                if count_zero == self.algorithm.number_of_objective - 1:
                    selection.append(w)
                    break

        xtrem_index = self.get_xtrem_index()

        #  10-tournament
        for i in range(int((self.algorithm.number_of_weight / 5) - self.algorithm.number_of_objective)):
            range_list = list(range(self.algorithm.number_of_weight))
            random_indexes = random.sample(list(set(range_list) - set(xtrem_index)), 10)

            best_index = random_indexes[0]
            best_pi = self.algorithm.pi[random_indexes[0]]
            for index in random_indexes:
                if self.algorithm.pi[index] > best_pi:
                    best_index = index
                    best_pi = self.algorithm.pi[index]

            selection.append(best_index)

        return selection

    def get_xtrem_index(self):
        """
        get boundaries sub-problems

        :return: {list<integer>} indexes of sub-problems
        """
        xtrem_index = []
        for i in range(self.algorithm.number_of_weight):
            weight = self.algorithm.weights[i]
            for j in range(self.algorithm.number_of_objective):
                if weight[j] == 1:
                    xtrem_index.append(i)
                    break

        return xtrem_index
