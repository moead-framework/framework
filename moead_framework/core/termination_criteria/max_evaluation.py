from moead_framework.core.termination_criteria.abstract_termination_criteria import TerminationCriteria


class MaxEvaluation(TerminationCriteria):
    """
    Stop the algorithm with a criteria based on the number of solution evaluated.
    """

    def test(self):
        """
        Test if the algorithm has to be stopped. The algorithm is stopped when the maximum
        number of evaluation is reached

        :return: {boolean} True: Continue the process. False: Stop the process
        """
        return self.algorithm.current_eval <= self.algorithm.max_evaluation
