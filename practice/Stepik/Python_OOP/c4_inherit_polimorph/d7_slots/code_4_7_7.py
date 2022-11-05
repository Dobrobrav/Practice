from typing import Dict, Any


class Note:
    _name: str
    _ton: int

    def __init__(self, name: str, ton: int):
        self.name = name
        self.ton = ton

    def __setattr__(self, key: str, value: Any):
        if key == '_name':
            self._validate_name(value)
        elif key == '_ton':
            self._validate_ton(value)
        super().__setattr__(key, value)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._validate_name(name)
        self._name = name

    @property
    def ton(self) -> int:
        return self._ton

    @ton.setter
    def ton(self, ton: int):
        self._validate_ton(ton)
        self._ton = ton

    @staticmethod
    def _validate_ton(ton: int):
        if ton not in (-1, 0, 1):
            raise ValueError('недопустимое значение аргумента')

    @staticmethod
    def _validate_name(name: str):
        if name not in ("до", "ре", "ми", "фа", "соль", "ля", "си"):
            raise ValueError('недопустимое значение аргумента')


class MetaSingleton(type):
    _instances: Dict[type, Any] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls) \
                .__call__(*args, **kwargs)

        return cls._instances[cls]


class Notes(metaclass=MetaSingleton):
    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')
    _CYRILLIC_NOTES = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')

    def __init__(self):
        for attr_name, note_name_ru in zip(self.__slots__, self._CYRILLIC_NOTES):
            setattr(self, attr_name, Note(note_name_ru, ton=0))

    def __setitem__(self, index: int, ton: int):
        self._validate_index(ton)
        note_name = self.__slots__[index]
        note: Note = getattr(self, note_name)
        note.ton = ton

    def __getitem__(self, index: int) -> Note:
        self._validate_index(index)
        note_name = self.__slots__[index]
        return getattr(self, note_name)

    @staticmethod
    def _validate_index(index: int):
        if not (type(index) is int and 0 <= index <= 6):
            raise IndexError('недопустимый индекс')


if __name__ == '__main__':
    notes = Notes()
