class ResultFormatUtility:
    @staticmethod
    def str_repr(items: list):
        result = []
        for item in items:
            result.append(f'{item}')
        return result
