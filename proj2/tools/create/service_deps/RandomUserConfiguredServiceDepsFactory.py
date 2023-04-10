from proj2.tools.service_deps.ConfiguredServiceDeps import ConfiguredServiceDeps
from proj2.tools.props_read.AppConfigItem import AppConfigItem
from proj2.tools.const.ConfigConsts import ConfiguredServiceDepsConsts
from proj2.tools.create.user.RandomUserFactory import RandomUserFactory
from proj2.tools.loader.RandomUserDataLoader import RandomUserDataLoader

from proj2.tools.init_item.InitStrategy import InitStrategy
from proj2.tools.init_item.RandomUserSinglePropInitStrategy import RandomUserSinglePropInitStrategy
from proj2.tools.init_item.ListOfPropPairsIntStrategy import ListOfPropPairsIntStrategy
from proj2.tools.calc.RandomUserCalcAlgorithm import RandomUserCalcAlgorithm


class RandomUserConfiguredServiceDepsFactory():
    def __init__(self, app_config_item: AppConfigItem):
        self.app_config_item = app_config_item

    def create(self) -> ConfiguredServiceDeps:
        configured_service_deps = ConfiguredServiceDeps({
            ConfiguredServiceDepsConsts.DATA_LOADER_TYPE: RandomUserDataLoader(self.app_config_item),
            ConfiguredServiceDepsConsts.INIT_STRATEGY_TYPE: self.__build_init_strategy(),
            ConfiguredServiceDepsConsts.USER_FACTORY_TYPE: RandomUserFactory(),
            ConfiguredServiceDepsConsts.CALC_ALGORITHM_TYPE: RandomUserCalcAlgorithm()
        })
        return configured_service_deps

    def __build_init_strategy(self) -> InitStrategy:
        prop_names = ["id.value", "name.last", "name.first"]
        single_prop_initializers = []
        for prop_name in prop_names:
            single_prop_initializers.append(RandomUserSinglePropInitStrategy(prop_name))
        return ListOfPropPairsIntStrategy(single_prop_initializers)
