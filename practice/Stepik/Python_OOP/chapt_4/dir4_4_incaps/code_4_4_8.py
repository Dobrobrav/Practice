from typing import Any, Dict


class PositiveNumber:
    def __set_name__(self, owner: type, name: str):
        self.name = f"_{name}"

    def __set__(self, instance: Any, value: float):
        self._validate_positive_number(value)
        setattr(instance, self.name, value)

    def __get__(self, instance: Any, owner: type):
        return getattr(instance, self.name)

    @staticmethod
    def _validate_positive_number(value: float):
        if not (type(value) in (int, float) and value > 0):
            raise TypeError('неверный тип аргумента')


class Aircraft:
    _model: str
    mass = PositiveNumber()
    speed = PositiveNumber()
    top = PositiveNumber()

    def __init__(self, model: str, mass: float, speed: float, top: float):
        self.model = model
        self.mass = mass
        self.speed = speed
        self.top = top

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, model: str):
        self._validate_type(model, type_=str)
        self._model = model

    @staticmethod
    def _validate_type(value: Any, type_: type):
        if type(value) is not type_:
            raise TypeError('неверный тип аргумента')


class PassengerAircraft(Aircraft):
    _chairs: int

    def __init__(self, model: str, mass: float, speed: float,
                 top: float, chairs: int):
        super().__init__(model, mass, speed, top)
        self.chairs = chairs

    @property
    def chairs(self) -> int:
        return self._chairs

    @chairs.setter
    def chairs(self, chairs: int):
        self._validate_type(chairs, type_=int)


class WarPlane(Aircraft):
    _weapons: Dict[str, int]

    def __init__(self, model: str, mass: float, speed: float,
                 top: float, weapons: Dict[str, int]):
        super().__init__(model, mass, speed, top)
        self.weapons = weapons

    @property
    def weapons(self) -> Dict[str, int]:
        return self._weapons

    @weapons.setter
    def weapons(self, weapons: Dict[str, int]):
        self._validate_weapons(weapons)
        self._weapons = weapons

    def _validate_weapons(self, weapons: Dict[str, int]):
        self._validate_type(weapons, dict)
        for key, value in weapons.items():
            self._validate_type(key, type_=str)
            self._validate_type(value, type_=int)


if __name__ == '__main__':
    planes = [
        PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
        PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
        WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
        WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})
    ]
