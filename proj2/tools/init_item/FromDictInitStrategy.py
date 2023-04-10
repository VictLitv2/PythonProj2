from proj2.tools.init_item.InitStrategy import InitStrategy
from proj2.tools.model.User import User


class FromDictInitStrategy(InitStrategy):
    def __init__(self):
        pass

    def init_state(self, user: User, user_dict: dict) -> User:
        user.__setattr__("__dict__", user_dict)
        return user
