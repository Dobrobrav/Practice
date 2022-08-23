from typing import Optional


class Observer:
    def update(self, data: 'Data'):
        pass

    def __hash__(self):
        return hash(id(self))


class Subject:
    __observers: dict
    __data: Optional['Data']

    def __init__(self):
        self.__observers = {}
        self.__data = None

    def add_observer(self, observer: Observer):
        self.__observers[observer] = observer

    def remove_observer(self, observer: Observer):
        if observer in self.__observers:
            self.__observers.pop(observer)

    def __notify_observer(self):
        for ob in self.__observers:
            ob.update(self.__data)

    def change_data(self, data: 'Data'):
        self.__data = data
        self.__notify_observer()


class Data:
    temp: float
    press: float
    wet: float

    def __init__(self, temp: float, press: float, wet: float):
        self.temp = temp  # температура
        self.press = press  # давление
        self.wet = wet  # влажность


# здесь объявляйте дочерние классы TemperatureView, PressureView и WetView

class TemperatureView(Observer):
    def update(self, data: Data):
        print(f"Текущая температура {round(data.temp, 2)}")


class PressureView(Observer):
    def update(self, data: Data):
        print(f"Текущее давление {round(data.press, 2)}")


class WetView(Observer):
    def update(self, data: Data):
        print(f"Текущая влажность {round(data.wet, 2)}")
