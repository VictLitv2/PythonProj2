from unittest import TestCase
from proj2.tools.service.MainAppLogic import MainAppLogic

class MainAppLogicTestCase(TestCase):

    def test_resolve_service_definition(self):
        main_app_logic = MainAppLogic(config_file_path="../../../../config.yaml")
        result = main_app_logic.process_logic()
        self.assertIsNotNone(result)

