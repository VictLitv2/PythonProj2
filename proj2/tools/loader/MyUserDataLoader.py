from proj2.tools.loader.DataLoader import DataLoader

from proj2.tools.props_read.AppConfigItem import AppConfigItem


class MyUserDataLoader(DataLoader):
    def __init__(self, app_config_item: AppConfigItem):
        # base url taken from outside property or config

        base_url = app_config_item.get_url()
        self.url = f"{base_url}"

    def with_user_search_params(self, user_search_params: dict):
        base_url_str = self.url
        total_length_base_url = len(base_url_str)
        last_idx_slash = base_url_str.rindex("/")
        if (last_idx_slash == total_length_base_url - 1):
            base_url_str = base_url_str[0:last_idx_slash]
        name_param = user_search_params.get("name")
        self.url = f"{base_url_str}?name={name_param}"
        return self

    def get_url(self):
        return self.url
