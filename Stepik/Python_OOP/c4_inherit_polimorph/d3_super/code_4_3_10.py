from typing import Tuple, Any


class ItemAttrs:
    _attr_name_by_id: Tuple[str, ...]

    def __init__(self):
        self._attr_name_by_id = tuple(self.__dict__)

    def __getitem__(self, item: int):
        attr_name = self._attr_name_by_id[item]
        return getattr(self, attr_name)

    def __setitem__(self, key: int, value: Any):
        attr_name = self._attr_name_by_id[key]
        setattr(self, attr_name, value)


class Point(ItemAttrs):
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        super(Point, self).__init__()
