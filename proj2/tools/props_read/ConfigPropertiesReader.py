import yaml
import json

from proj2.tools.props_read.AppConfigItem import AppConfigItem


class ConfigPropertiesReader:
    def read_props(self, path) -> dict:
        with open(path) as yaml_config_file:
            config_props = yaml.safe_load(yaml_config_file)

            app_config_items = []
            for app_config_item_key in config_props.keys():
                app_config_item_props = config_props.get(app_config_item_key)
                app_config_item = AppConfigItem(app_config_item_props)
                app_config_items.append(app_config_item)
            return config_props
