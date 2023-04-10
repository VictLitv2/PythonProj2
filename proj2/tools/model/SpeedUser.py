# from _distutils_hack import override
from proj2.tools.model.User import User


class SpeedUser(User):
    def __init__(self, dict: dict = {}):
        self.__dict__ = dict

    def __str__(self):
        return f"{self.__dict__}"

    def get_id(self):
        return self.id
