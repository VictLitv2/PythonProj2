from unittest import TestCase
from proj2.tools.init_item.ListOfPropPairsIntStrategy import ListOfPropPairsIntStrategy
from proj2.tools.init_item.SinglePropInitStrategy import SinglePropInitStrategy
from proj2.tools.model.MyUser import MyUser
class ListOfPropPairsIntStrategyTestCase(TestCase):

    def test_init_state(self):
        #given
        prop_names =  ["id","name","username","email"]
        single_prop_initializers = []
        for prop_name in prop_names:
            single_prop_initializers.append(SinglePropInitStrategy(prop_name))

        init_strategy = ListOfPropPairsIntStrategy(single_prop_initializers)

        user = MyUser()
        from_json_dict = {"id":"1","name":"John Smith","username":"jsmith","email":"jsmith@gumail.com"}
        # when
        result_user = init_strategy.init_state(user,from_json_dict)
        #self.fail()
        # then
        print(f"initialized props of user {result_user.__dict__.keys()}")
        self.assertListEqual(sorted(prop_names),sorted(result_user.__dict__.keys()))
        self.assertDictEqual(from_json_dict,result_user.__dict__)