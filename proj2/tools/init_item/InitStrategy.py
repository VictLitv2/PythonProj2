from abc import ABC
from proj2.tools.model.User import User
class InitStrategy(ABC):
    def init_state(self,src_obj:User,init_data:object=None) -> User:
        raise NotImplementedError