from proj2.tools.model.User import User


class MyUser(User):
    id = None
    name = None
    email = None
    username = None

    def __str__(self) -> str:
        return f"id={self.id},name={self.name},email={self.email},username={self.username}"

    def __init__(self):
        pass

    def get_id(self):
        return self.id
