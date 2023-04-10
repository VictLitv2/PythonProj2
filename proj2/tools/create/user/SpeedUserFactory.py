from proj2.tools.create.user.UserFactory import UserFactory
from proj2.tools.model.SpeedUser import SpeedUser
from proj2.tools.model.User import User

class SpeedUserFactory(UserFactory):
    def __init__(self):
        pass

    def create_user(self) -> User:
        return SpeedUser()