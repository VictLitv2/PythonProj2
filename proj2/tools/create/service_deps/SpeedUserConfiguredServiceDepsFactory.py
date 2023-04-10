from proj2.tools.create.service_deps.ConfiguredServiceDepsFactory import ConfiguredServiceDepsFactory
from proj2.tools.service_deps.ConfiguredServiceDeps import ConfiguredServiceDeps
from proj2.tools.props_read.AppConfigItem import AppConfigItem
from proj2.tools.const.ConfigConsts import ConfiguredServiceDepsConsts
from proj2.tools.create.user.SpeedUserFactory import SpeedUserFactory
from proj2.tools.loader.SpeedUserDataLoader import SpeedUserDataLoader

from proj2.tools.init_item.InitStrategy import InitStrategy
from proj2.tools.init_item.FromDictInitStrategy import FromDictInitStrategy
from proj2.tools.calc.SpeedUserCalcAlgorithm import SpeedUserCalcAlgorithm

class SpeedUserConfiguredServiceDepsFactory(ConfiguredServiceDepsFactory):
    def __init__(self, app_config_item: AppConfigItem):
        self.app_config_item = app_config_item
    def create(self) -> ConfiguredServiceDeps:
        configured_service_deps = ConfiguredServiceDeps({
            ConfiguredServiceDepsConsts.DATA_LOADER_TYPE: SpeedUserDataLoader(self.app_config_item),
            ConfiguredServiceDepsConsts.INIT_STRATEGY_TYPE: self.__build_init_strategy(),
            ConfiguredServiceDepsConsts.USER_FACTORY_TYPE: SpeedUserFactory(),
            ConfiguredServiceDepsConsts.CALC_ALGORITHM_TYPE: SpeedUserCalcAlgorithm()

        })
        return configured_service_deps

    def __build_init_strategy(self) -> InitStrategy:
        return FromDictInitStrategy()

