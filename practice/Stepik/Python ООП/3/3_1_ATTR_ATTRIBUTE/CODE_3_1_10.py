from typing import Optional, Tuple
import time


class FilterCartridge:
    _date: float

    def __init__(self, date: float):
        self._date = date

    @property
    def date(self) -> float:
        return self._date

    @date.setter
    def date(self, date: float) -> None:
        pass


class Mechanical(FilterCartridge):
    def __init__(self, date: float):
        super().__init__(date)


class Aragon(FilterCartridge):
    def __init__(self, date: float):
        super().__init__(date)


class Calcium(FilterCartridge):
    def __init__(self, date: float):
        super().__init__(date)


class GeyserClassic:
    cartridges_for_slots = {
        1: Mechanical,
        2: Aragon,
        3: Calcium,
    }
    MAX_DATE_FILTER = 100
    slot_1: Optional[Mechanical] = None
    slot_2: Optional[Aragon] = None
    slot_3: Optional[Calcium] = None

    def add_filter(self, slot_num: int, filter: FilterCartridge) -> None:
        if (getattr(self, f"slot_{slot_num}") is None
                and type(filter) is self.cartridges_for_slots[slot_num]):
            setattr(self, f"slot_{slot_num}", filter)

    def remove_filter(self, slot_num: int) -> FilterCartridge:
        return_slot = getattr(self, f"slot_{slot_num}")
        delattr(self, f"slot_{slot_num}")
        return return_slot

    def get_filters(self) -> Tuple[Optional[FilterCartridge], ...]:
        return (
            self.slot_1,
            self.slot_2,
            self.slot_3,
        )

    def water_on(self) -> bool:
        return all(
            cartridge
            and 0 <= time.time() - cartridge.date <= self.MAX_DATE_FILTER
            for cartridge in (self.slot_1, self.slot_2, self.slot_3)
        )
