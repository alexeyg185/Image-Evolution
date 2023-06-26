import abc
from GlobalDefintions import *


# -------------------------------------------------------------------------------------------------
# OptimizationSchemeContext BEG
# Encapsulates OptimizationScheme implementations
# -------------------------------------------------------------------------------------------------
class OptimizationSchemeContext:

    def __init__(self, strategy):
        self._strategy = strategy

    def run(self):
        self._strategy.find_solution()
# -------------------------------------------------------------------------------------------------
# OptimizationSchemeContext END
# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
# OptimizationSchemeStrategy BEG
# -------------------------------------------------------------------------------------------------
class OptimizationSchemeStrategy(abc.ABC):

    @abc.abstractmethod
    def find_solution(self):
        pass
# -------------------------------------------------------------------------------------------------
# OptimizationSchemeStrategy BEG
# -------------------------------------------------------------------------------------------------


