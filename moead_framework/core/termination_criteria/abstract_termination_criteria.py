from abc import ABC, abstractmethod


class TerminationCriteria(ABC):
    """
    Component used to stop the algorithm
    """

    def __init__(self, algorithm_instance):
        """
        Constructor of the termination criteria

        :param algorithm_instance: {:class:`~moead_framework.algorithm.abstract_moead.py.AbstractMoead`} instance of the algorithm
        """
        self.algorithm = algorithm_instance

    @abstractmethod
    def test(self):
        """
        Test if the algorithm has to be stopped

        :return: {boolean} True: Continue the process. False: Stop the process
        """
