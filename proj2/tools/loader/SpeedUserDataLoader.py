from proj2.tools.loader.DataLoader import DataLoader
from proj2.tools.props_read.AppConfigItem import AppConfigItem


class SpeedUserDataLoader(DataLoader):
    def __init__(self, app_config_item: AppConfigItem):
        self.url = app_config_item.get_url()

    def with_user_search_params(self, user_search_params: dict):
        self.req_params = user_search_params

    def get_url(self):
        return self.url

    def get_req_params(self):
        return self.req_params
