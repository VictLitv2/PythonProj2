from abc import ABC, abstractmethod
class User(ABC):
    @abstractmethod
    def get_id(self):
        raise NotImplementedError
