from proj2.tools.model.User import User


class SimpleUser(User):
    def __init__(self):
        pass

    def get_id(self):
        return self.id
