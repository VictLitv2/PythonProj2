from proj2.tools.calc.CalcAlgorithm import CalcAlgorithm
from proj2.tools.const.ConfigConsts import UserSearchParams
from proj2.tools.calc.ResultFormatUtility import ResultFormatUtility

class RandomUserCalcAlgorithm(CalcAlgorithm):
    def __init__(self):
        pass

    def calculate(self, all_results_from_site):

        return ResultFormatUtility.str_repr(all_results_from_site)


    def provide_additional_user_params(self):
        total_tries_str = None
        self.total_tries = None
        while self.total_tries is None or type(self.total_tries) != int:
            total_tries_str = input(
                "Please enter number of tries to search random user on  site `randomuser.me`\n")
            self.total_tries = int(total_tries_str.replace(' ', ''))
        return {UserSearchParams.RANDOM_USER_NUM_OF_SEARCHES: str(self.total_tries)}