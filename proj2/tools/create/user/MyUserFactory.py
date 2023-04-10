from proj2.tools.create.user.UserFactory import UserFactory
from proj2.tools.model.MyUser import MyUser
from proj2.tools.model.User import User
class MyUserFactory(UserFactory):
    def create_user(self) -> User:
        return MyUser()
