from proj2.tools.calc.CalcAlgorithm import CalcAlgorithm
from proj2.tools.model.LatitudeDiff import LatitudeDiff
from proj2.tools.model.SpeedUser import SpeedUser
from proj2.tools.calc.ResultFormatUtility import ResultFormatUtility

class SpeedUserCalcAlgorithm(CalcAlgorithm):
    def __init__(self):
        self.latitude_diffs = []

    def calculate(self, all_results_from_site):
        calculated_results = []
        for result_from_site in all_results_from_site:
            speed_user: SpeedUser = result_from_site
            found_lat = speed_user.address.get("geo").get("lat")
            if self.latitude == float(found_lat):
                calculated_results.append(speed_user)
            else:
                self.latitude_diffs.append(LatitudeDiff((self.latitude - float(found_lat)), speed_user.get_id()))

        if len(calculated_results) != 0:
            return ResultFormatUtility.str_repr(calculated_results)

        calculated_results = self.__calculate_with_min_lat_diff(all_results_from_site)
        return ResultFormatUtility.str_repr(calculated_results)

    def __calculate_with_min_lat_diff(self, all_results_from_site):

        sorted(self.latitude_diffs, key=lambda latitude_diff: latitude_diff.diff, reverse=True)
        minimal_latitude_diff = self.latitude_diffs[0]
        for result_from_site in all_results_from_site:
            speed_user: SpeedUser = result_from_site
            if speed_user.get_id() == minimal_latitude_diff.user_id:
                return [speed_user]
        return []



    def provide_additional_user_params(self):
        latitude_str = None
        self.latitude = None
        while self.latitude is None or type(self.latitude) != float:
            latitude_str = input(
                "Please enter user's latitude  to search on site\n(it should be number or fraction with dot)\n")
            try:
                self.latitude = float(latitude_str.replace(' ', ''))
            except:
                print("Error occured")
        return {"lat": str(self.latitude)}
