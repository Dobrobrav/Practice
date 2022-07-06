class Model:
    def query(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    def __str__(self):
        if not self.__dict__:
            return "Model"
        repr_string = "Model: "+', '.join((
            f"{field} = {value}"
            for field, value in self.__dict__.items()
        ))
        return repr_string


if __name__ == '__main__':
    model = Model()
    model.query(id=1, fio='Sergey', old=33)

    print(model.__dict__)
    print(model)
