from proj2.tools.calc.CalcAlgorithm import CalcAlgorithm
from proj2.tools.model.LatitudeDiff import LatitudeDiff
from proj2.tools.model.SpeedUser import SpeedUser
from proj2.tools.calc.ResultFormatUtility import ResultFormatUtility
import math
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
                calc_diff = self.__calculate_diff(self.latitude, float(found_lat))

                self.latitude_diffs.append(LatitudeDiff(calc_diff, speed_user.get_id()))

        if len(calculated_results) != 0:
            return ResultFormatUtility.str_repr(calculated_results)

        calculated_results = self.__calculate_with_min_lat_diff(all_results_from_site)
        self.latitude = None
        self.latitude_diffs = []

        return ResultFormatUtility.str_repr(calculated_results)
    def __calculate_diff(self,a,b):
        sign = lambda x: math.copysign(1, x)
        if sign(a) == sign (b):
            return  math.fabs(a) - math.fabs(b)
        return  math.fabs(a - b)

    def __calculate_with_min_lat_diff(self, all_results_from_site):

        sorted_lattitude_diffs = sorted(self.latitude_diffs, key=lambda latitude_diff: math.fabs(latitude_diff.diff), reverse=False)
        minimal_latitude_diff = sorted_lattitude_diffs[0]

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
