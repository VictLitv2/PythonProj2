from abc import ABC, abstractmethod

import requests


class DataLoader(ABC):

    def load_as_json(self):
        data = requests.get(self.get_url(), params=self.get_req_params())
        user_elems = data.json()

        return user_elems

    @abstractmethod
    def with_user_search_params(self, user_search_params: dict):
        raise NotImplementedError

    @abstractmethod
    def get_url(self):
        raise NotImplementedError

    def get_req_params(self):
        return {}
