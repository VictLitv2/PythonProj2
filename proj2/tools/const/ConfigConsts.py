from  proj2.tools.loader.DataLoader import DataLoader
from proj2.tools.create.user.UserFactory import UserFactory
from  proj2.tools.init_item.InitStrategy import InitStrategy
from  proj2.tools.calc.CalcAlgorithm import CalcAlgorithm
class ConfigConsts:
    pass

class WorkflowCases:
    MY_USER = "my_user_case"
    RANDOM_USER = "random_user_case"
    SPEED_USER = "speed_user_case"
class AlgorithmType:
    TYPE_PROP_NAME = "calc_algorithm_type"
    MY_USER = 1
    SPEED_USER = 2
    RANDOM_USER = 3
class ConfiguredServiceDepsConsts:
    DATA_LOADER_TYPE = DataLoader.__name__
    USER_FACTORY_TYPE = UserFactory.__name__
    INIT_STRATEGY_TYPE = InitStrategy.__name__
    CALC_ALGORITHM_TYPE = CalcAlgorithm.__name__
class UserSearchParams:
    RANDOM_USER_NUM_OF_SEARCHES = "total_users_to_find"