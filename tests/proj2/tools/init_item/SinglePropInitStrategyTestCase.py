from unittest import TestCase
from proj2.tools.model.SimpleUser import SimpleUser

from proj2.tools.init_item.InitStrategy import InitStrategy
from  proj2.tools.init_item.SinglePropInitStrategy import SinglePropInitStrategy

class SinglePropInitStrategyTestCase(TestCase):
    def test_init_state(self):
        #given
        user = SimpleUser()
        from_json_dict = {"prop1": "1"}
        initStrategy = SinglePropInitStrategy("prop1")


        #when
        user2 = initStrategy.init_state(user,from_json_dict)#, pair1


        #then
        self.assertIsNotNone(user)
        pair1 = ("prop1", "1")
        self.assertEqual(str(pair1[1]), user2.__getattribute__(pair1[0]))
