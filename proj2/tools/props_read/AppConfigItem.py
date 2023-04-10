class AppConfigItem:
    def __init__(self, item_props_as_dict: dict):
        self.__dict__ = item_props_as_dict

    def __str__(self):
        return f"{self.__dict__}"

    def get_url(self):
        return self.url
