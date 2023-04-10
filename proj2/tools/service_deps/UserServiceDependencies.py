from proj2.tools.loader.DataLoader import DataLoader
from proj2.tools.create.user.UserFactory import UserFactory
from proj2.tools.init_item.InitStrategy import InitStrategy
from proj2.tools.calc.CalcAlgorithm import CalcAlgorithm
from abc import ABC


class UserServiceDependencies(ABC):

    def with_user_data_loader(self, user_data_loader: DataLoader):
        self.user_data_loader = user_data_loader
        return self

    def with_user_factory(self, user_factory: UserFactory):
        self.user_factory = user_factory
        return self

    def with_init_strategy(self, init_strategy: InitStrategy):
        self.init_strategy = init_strategy
        return self

    def with_calc_algorithm(self, calc_algorithm: CalcAlgorithm):
        self.calc_algorithm = calc_algorithm
        return self
