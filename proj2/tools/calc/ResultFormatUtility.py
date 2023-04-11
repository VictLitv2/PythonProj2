class ResultFormatUtility:
    @staticmethod
    def str_repr(items: list):
        result = []
        for item in items:
            item_str = str(item).encode(encoding="utf-8")
            result.append(item_str)
        return result
