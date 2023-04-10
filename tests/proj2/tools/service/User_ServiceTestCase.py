from unittest import TestCase
from proj2.tools.service.UserService import UserService
from proj2.tools.loader.MyUserDataLoader import MyUserDataLoader
from proj2.tools.create.user.MyUserFactory import MyUserFactory
from proj2.tools.init_item.ListOfPropPairsIntStrategy import ListOfPropPairsIntStrategy
from proj2.tools.init_item.SinglePropInitStrategy import SinglePropInitStrategy
from proj2.tools.calc.MyUserCalcAlgorithm import MyUserCalcAlgorithm
from proj2.tools.props_read.AppConfigItem import AppConfigItem
#non-mocking integration test of this project's service layer
class User_ServiceTestCase(TestCase):


    def test_get_final_result_should_find_user(self):
        self.handle_common_test_case("Leanne Graham", lambda result: self.assertNotEqual(result, "User not found"))

    def test_get_final_result_should_not_find_user(self):
        self.handle_common_test_case("Lemmie", lambda result: self.assertEqual(result, "User not found"))

    def handle_common_test_case(self,user_name,handle_result_case):
        app_config_item = AppConfigItem({"url":"https://jsonplaceholder.typicode.com/users/"})

        data_loader = MyUserDataLoader(app_config_item) \
            .with_user_search_params({"name": user_name})
        user_factory = MyUserFactory()
        prop_names = ["id", "name", "username", "email"]
        single_prop_initializers = []
        for prop_name in prop_names:
            single_prop_initializers.append(SinglePropInitStrategy(prop_name))
        init_strategy = ListOfPropPairsIntStrategy(single_prop_initializers)
        calc_algorithm = MyUserCalcAlgorithm()
        user_service = UserService() \
            .with_user_data_loader(data_loader) \
            .with_user_factory(user_factory) \
            .with_init_strategy(init_strategy) \
            .with_calc_algorithm(calc_algorithm)
        result = user_service.get_final_result()
        #self.assertNotEqual(result, None)

        handle_result_case(result)