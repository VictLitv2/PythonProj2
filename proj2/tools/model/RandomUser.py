class RandomUser:
    id_value = None
    name_last = None
    name_first = None

    def __str__(self) -> str:
        return f"id={self.id_value},name={self.name_last} {self.name_first}"

    def get_id(self):
        return self.id_value
