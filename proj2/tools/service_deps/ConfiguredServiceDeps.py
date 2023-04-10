from proj2.tools.service_deps.UserServiceDependencies import UserServiceDependencies
from proj2.tools.const.ConfigConsts import ConfiguredServiceDepsConsts


class ConfiguredServiceDeps(UserServiceDependencies):
    def __init__(self, deps: dict):
        self.with_calc_algorithm(deps.get(ConfiguredServiceDepsConsts.CALC_ALGORITHM_TYPE))
        self.with_user_factory(deps.get(ConfiguredServiceDepsConsts.USER_FACTORY_TYPE))
        self.with_init_strategy(deps.get(ConfiguredServiceDepsConsts.INIT_STRATEGY_TYPE))
        self.with_user_data_loader(deps.get(ConfiguredServiceDepsConsts.DATA_LOADER_TYPE))
