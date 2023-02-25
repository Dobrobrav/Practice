from typing import Optional


class ObjList:
    __prev: 'Optional[ObjList]' = None
    __next: 'Optional[ObjList]' = None
    __data: str

    def __init__(self, data: str):
        self.__data = data

    def __repr__(self):
        return self.data

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj: 'ObjList'):
        if isinstance(obj, ObjList):
            self.__prev = obj

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj: 'ObjList'):
        if isinstance(obj, ObjList):
            self.__next = obj

    @next.deleter
    def next(self):
        del self.__next

    @property
    def data(self):
        return self.__data


class LinkedList:
    head: 'Optional[ObjList]' = None
    tail: 'Optional[ObjList]' = None
    _length: int = 0

    def __len__(self) -> int:
        return self._length

    def __call__(self, indx: int, *args, **kwargs) -> str:
        obj = self._find_obj(indx)
        return obj.data if obj is not None else None
        # return None if obj is None else obj.data

    def add_obj(self, obj: ObjList):
        self._length += 1
        if self.head is None:
            self.head = self.tail = obj
        else:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj

    def remove_obj(self, indx: int) -> None:
        obj = self._find_obj(indx)
        if obj is None:
            return
        if obj.next is None:
            del obj.prev.next
            self.tail = obj.prev
        else:
            obj.prev.next = obj.next
            obj.next.prev = obj.prev
        self._length -= 1

    def _find_obj(self, indx: int) -> Optional[ObjList]:
        if indx < 0:
            indx = indx + len(self)
        if len(self) - indx < 1:
            return None
        if indx <= len(self) // 2:
            return self._forward_search(indx)
        return self._backward_search(indx)

    def _forward_search(self, indx: int) -> Optional[ObjList]:
        obj = self.head
        for _ in range(indx):
            if obj is None:
                return None
            obj = obj.next
        return obj

    def _backward_search(self, indx: int) -> Optional[ObjList]:
        obj = self.tail
        for _ in range(len(self) - 1, indx, -1):  # would be nice to use __next__
            obj = obj.prev
        return obj
