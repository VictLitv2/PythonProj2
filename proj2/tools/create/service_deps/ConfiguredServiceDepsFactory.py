from proj2.tools.service_deps.ConfiguredServiceDeps import ConfiguredServiceDeps
from proj2.tools.props_read.AppConfigItem import AppConfigItem
from abc import ABC, abstractmethod
class ConfiguredServiceDepsFactory(ABC):
    def create(self)->ConfiguredServiceDeps:
        raise NotImplementedError