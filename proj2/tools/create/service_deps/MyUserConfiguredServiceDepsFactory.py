from proj2.tools.create.service_deps.ConfiguredServiceDepsFactory import ConfiguredServiceDepsFactory
from proj2.tools.service_deps.ConfiguredServiceDeps import ConfiguredServiceDeps
from proj2.tools.props_read.AppConfigItem import AppConfigItem
from proj2.tools.const.ConfigConsts import ConfiguredServiceDepsConsts
from proj2.tools.create.user.MyUserFactory import MyUserFactory
from proj2.tools.loader.MyUserDataLoader import MyUserDataLoader

from proj2.tools.init_item.InitStrategy import InitStrategy
from proj2.tools.init_item.SinglePropInitStrategy import SinglePropInitStrategy
from proj2.tools.init_item.ListOfPropPairsIntStrategy import ListOfPropPairsIntStrategy
from proj2.tools.calc.MyUserCalcAlgorithm import MyUserCalcAlgorithm
class MyUserConfiguredServiceDepsFactory(ConfiguredServiceDepsFactory):
    def __init__(self,app_config_item: AppConfigItem):
        self.app_config_item = app_config_item
    def create(self) -> ConfiguredServiceDeps:
        configured_service_deps = ConfiguredServiceDeps({
            ConfiguredServiceDepsConsts.DATA_LOADER_TYPE: MyUserDataLoader( self.app_config_item),
            ConfiguredServiceDepsConsts.INIT_STRATEGY_TYPE: self.__build_init_strategy(),
            ConfiguredServiceDepsConsts.USER_FACTORY_TYPE: MyUserFactory(),
            ConfiguredServiceDepsConsts.CALC_ALGORITHM_TYPE: MyUserCalcAlgorithm()
        })
        return configured_service_deps

    def __build_init_strategy(self) -> InitStrategy:
        prop_names = ["id", "name", "username", "email"]
        single_prop_initializers = []
        for prop_name in prop_names:
            single_prop_initializers.append(SinglePropInitStrategy(prop_name))
        return ListOfPropPairsIntStrategy(single_prop_initializers)
