from proj2.tools.init_item.InitStrategy import InitStrategy
from proj2.tools.model.User import User


class SinglePropInitStrategy(InitStrategy):
    def __init__(self, prop_name: str):
        self.prop_name = prop_name
        # self.from_json_dict = from_json_dict
        pass

    def init_state(self, user: User, from_json_dict: dict) -> User:
        # user.__setattr__("__dict__", self.user_dict)

        prop_name_and_value_pair = (self.prop_name, from_json_dict.get(self.prop_name))
        prop_name = prop_name_and_value_pair[0]
        prop_val = prop_name_and_value_pair[1]
        user.__setattr__(prop_name, prop_val)
        return user
