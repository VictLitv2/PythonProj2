from proj2.tools.create.user.UserFactory import UserFactory
from proj2.tools.model.RandomUser import RandomUser
from proj2.tools.model.User import User

class RandomUserFactory(UserFactory):
    def create_user(self) -> User:
        return RandomUser()
