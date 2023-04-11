import codecs

from proj2.tools.service.UserService import UserService
from proj2.tools.props_read.ConfigPropertiesReader import ConfigPropertiesReader
from proj2.tools.const.ConfigConsts import ConfigConsts, WorkflowCases, AlgorithmType

from proj2.tools.props_read.AppConfigItem import AppConfigItem
from proj2.tools.create.service_deps.MyUserConfiguredServiceDepsFactory import MyUserConfiguredServiceDepsFactory
from proj2.tools.create.service_deps.SpeedUserConfiguredServiceDepsFactory import SpeedUserConfiguredServiceDepsFactory
from proj2.tools.create.service_deps.RandomUserConfiguredServiceDepsFactory import \
    RandomUserConfiguredServiceDepsFactory
from proj2.tools.create.service_deps.ConfiguredServiceDepsFactory import ConfiguredServiceDepsFactory

import codecs

class MainAppLogic():
    config_props = None

    def __init__(self, config_file_path="config.yaml"):  #
        self.serv_definition_by_app_config = {}

        self.config_props = self.__read_config(config_file_path)

        self.serv_definition_by_app_config = self.__init_service_definitions()

    def __init_service_definitions(self):
        my_user_app_config_item: AppConfigItem = AppConfigItem(self.config_props[WorkflowCases.MY_USER])
        speed_user_app_config_item: AppConfigItem = AppConfigItem(self.config_props[WorkflowCases.SPEED_USER])
        random_user_app_config_item: AppConfigItem = AppConfigItem(self.config_props[WorkflowCases.RANDOM_USER])

        return \
            {
                WorkflowCases.MY_USER: MyUserConfiguredServiceDepsFactory(my_user_app_config_item),
                WorkflowCases.SPEED_USER: SpeedUserConfiguredServiceDepsFactory(speed_user_app_config_item),
                WorkflowCases.RANDOM_USER: RandomUserConfiguredServiceDepsFactory(random_user_app_config_item)
            }

    def __read_config(self, config_file_path):
        props = ConfigPropertiesReader().read_props(config_file_path)

        return props

    def __process_input_param(self):
       case_num_str = None
       case_num = None
       while case_num is None or case_num not in range(1, 4):
            case_num_str = input(f"Please enter application workflow case numbered from 1 to 3\n")
            if not case_num_str.isnumeric():
                print("Error:Your input is not number")

            try:
                case_num = int(case_num_str)

                if not case_num in range(1, 4):
                    print("Error:Your input is not in possible range")

            except:
                print("Error")
       return case_num

    def __resolve_service_definition(self, user_input: int):
        # self.serv_definition_by_app_config
        for config_prop_key in self.config_props.keys():
            config_prop = self.config_props.get(config_prop_key)
            algorithm_type = int(config_prop.get(AlgorithmType.TYPE_PROP_NAME))
            if user_input == algorithm_type:
                return self.serv_definition_by_app_config.get(config_prop_key)
        return None

    def __init_service(self, service_deps_factory: ConfiguredServiceDepsFactory) -> UserService:
        configured_service_deps = service_deps_factory.create()
        # call copy constructor method chain from UserServiceDependencies mixin
        user_service = UserService() \
            .with_user_data_loader(configured_service_deps.user_data_loader) \
            .with_user_factory(configured_service_deps.user_factory) \
            .with_init_strategy(configured_service_deps.init_strategy) \
            .with_calc_algorithm(configured_service_deps.calc_algorithm)
        return user_service

    def __calculate(self, user_service: UserService):
        user_service.provide_additional_user_params()
        result = user_service.get_final_result()
        # print(f"Result:{result}")
        return result

    def process_logic(self):
        #
        # wait for user answer with prompt
        input_param_part = lambda empty: self.__process_input_param()
        resolve_service_definition_part = lambda user_input: self.__resolve_service_definition(user_input)
        init_service_part = lambda service_definition_params: self.__init_service(service_definition_params)
        calculate_part = lambda service_param: self.__calculate(service_param)

        logic_parts = [input_param_part, resolve_service_definition_part, init_service_part, calculate_part]
        logic_part_param = None
        for logic_part in logic_parts:
            logic_part_param = logic_part(logic_part_param)
        logic_result = logic_part_param
        print(f"Result of your search is:\n")
        try:
            for each_item in logic_result:
                print(codecs.decode(bytes(each_item)))
        except Exception as err:
                print (err)
        return logic_result
