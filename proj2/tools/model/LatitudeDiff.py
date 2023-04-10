class LatitudeDiff:
    def __init__(self, diff, user_id):
        self.diff = diff
        self.user_id = user_id

    def __repr__(self):
        return repr((self.diff, self.user_id))
