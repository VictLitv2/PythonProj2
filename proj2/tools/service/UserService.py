from proj2.tools.service_deps.UserServiceDependencies import UserServiceDependencies


class UserService(UserServiceDependencies):
    # users = None

    def __get_users(self):
        users = []
        user_elems = self.user_data_loader.load_as_json()
        for user_elem in user_elems:
            user = self.user_factory.create_user()

            self.init_strategy.init_state(user, user_elem)

            users.append(user)
        return users

    def get_final_result(self) -> object:
        users = self.__get_users()
        return self.calc_algorithm.calculate(users)

    def provide_additional_user_params(self):
        additional_params = self.calc_algorithm.provide_additional_user_params()
        self.user_data_loader.with_user_search_params(additional_params)
