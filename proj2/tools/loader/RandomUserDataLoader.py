from proj2.tools.loader.DataLoader import DataLoader
from proj2.tools.props_read.AppConfigItem import AppConfigItem
from proj2.tools.const.ConfigConsts import UserSearchParams


class RandomUserDataLoader(DataLoader):
    def __init__(self, app_config_item: AppConfigItem):
        self.url = app_config_item.get_url()
        self.user_search_params = None

    def with_user_search_params(self, user_search_params: dict):
        self.user_search_params = user_search_params

    def get_url(self):
        return self.url

    # overriding
    def load_as_json(self):
        user_elems = []

        num_of_searches = self.user_search_params.get(UserSearchParams.RANDOM_USER_NUM_OF_SEARCHES)
        for i in range(1, int(num_of_searches) + 1):
            one_req_result_tmp = super().load_as_json()
            one_req_result = one_req_result_tmp.get("results")[0]
            user_elems.append(one_req_result)
        return user_elems
