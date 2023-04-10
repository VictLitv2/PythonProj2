from proj2.tools.init_item.InitStrategy import InitStrategy
from proj2.tools.model.User import User


class RandomUserSinglePropInitStrategy(InitStrategy):
    def __init__(self, prop_name_path: str):
        self.prop_path = prop_name_path
        pass

    def init_state(self, user: User, from_json_dict: dict) -> User:
        prop_name_path_str = str(self.prop_path)
        prop_names_in_orig_order = prop_name_path_str.split('.')
        curr_dict = from_json_dict
        self.prop_value = None

        for prop_name in prop_names_in_orig_order:
            self.prop_value = curr_dict.get(prop_name)

            if type(self.prop_value) == dict:
                curr_dict = self.prop_value
                continue
        total_prop_name = prop_name_path_str.replace('.', '_')
        user.__setattr__(total_prop_name, self.prop_value)

        return user
