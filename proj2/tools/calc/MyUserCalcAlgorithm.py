from proj2.tools.calc.CalcAlgorithm import CalcAlgorithm
class MyUserCalcAlgorithm(CalcAlgorithm):
    def calculate(self, calc_params) ->object:
        if calc_params == None or len(calc_params) == 0:
            return "User not found"
        result = []
        for calc_param in calc_params:
            result.append(str(calc_param).encode(encoding="utf-8") )

        return result

    def provide_additional_user_params(self):
        user_full_name = input("Please enter user's first name and last name  to search on site\n")
        return {"name": user_full_name}
