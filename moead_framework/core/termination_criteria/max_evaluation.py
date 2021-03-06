from moead_framework.core.termination_criteria.abstract_termination_criteria import TerminationCriteria


class MaxEvaluation(TerminationCriteria):
    """
    Stop the algorithm with a criteria based on the number of solution evaluated.
    """

    def test(self):
        return self.algorithm.current_eval <= self.algorithm.max_evaluation
