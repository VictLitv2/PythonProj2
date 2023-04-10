from proj2.tools.init_item.InitStrategy import InitStrategy
from proj2.tools.init_item.SinglePropInitStrategy import SinglePropInitStrategy
from proj2.tools.model.User import User


class ListOfPropPairsIntStrategy(InitStrategy):
    def __init__(self, single_prop_strategies: list):
        self.single_prop_strategies = single_prop_strategies

    def init_state(self, src_obj: User, from_json_dict: dict) -> User:
        for single_prop_strategy in self.single_prop_strategies:
            tmp_single_prop_strategy: SinglePropInitStrategy = single_prop_strategy;
            tmp_single_prop_strategy.init_state(src_obj, from_json_dict);
        user = src_obj;
        return user
