from moead_framework.core.termination_criteria.abstract_termination_criteria import TerminationCriteria


class MaxEvaluation(TerminationCriteria):

    def __init__(self, algorithm_instance):
        super().__init__(algorithm_instance)

    def test(self):
        return self.algorithm.current_eval <= self.algorithm.max_evaluation
