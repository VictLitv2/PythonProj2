from abc import ABC, abstractmethod

class CalcAlgorithm(ABC):
    @abstractmethod
    def provide_additional_user_params(self) -> object:
        raise NotImplementedError
    @abstractmethod
    def calculate(self, calc_params) -> object:
        raise NotImplementedError
    