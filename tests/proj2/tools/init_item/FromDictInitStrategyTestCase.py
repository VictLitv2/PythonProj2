from unittest import TestCase
from proj2.tools.model.SpeedUser import SpeedUser
from  proj2.tools.init_item.FromDictInitStrategy import FromDictInitStrategy

class FromDictInitStrategyTestCase(TestCase):
    def test_init_state(self):
        #given

        #userFactory = SpeedUserFactory()
        #user = userFactory.create_user()
        user = SpeedUser()
        initStrategy = FromDictInitStrategy()
        dict1 = {"prop1": 1, "prop2": "2"}

        #when
        user2 = initStrategy.init_state(user, dict1)
        print(f"user {user}")

        #then
        self.assertIsNotNone(user)
        self.assertDictEqual(dict1, user2.__dict__)
