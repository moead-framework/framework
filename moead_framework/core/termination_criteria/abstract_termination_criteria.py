from abc import ABC, abstractmethod


class TerminationCriteria(ABC):
    """
    Component used to stop the algorithm
    """

    def __init__(self, algorithm_instance):
        self.algorithm = algorithm_instance

    @abstractmethod
    def test(self):
        """
        Test if the algorithm has to be stopped

        :return: {boolean}
        """
