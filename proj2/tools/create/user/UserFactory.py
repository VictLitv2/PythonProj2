from abc import ABC, abstractmethod
from proj2.tools.model.User import User
class UserFactory(ABC):
    @abstractmethod
    def create_user(self) -> User:
        raise NotImplementedError
