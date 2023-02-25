from typing import Optional, List


class WordString:
    _string: Optional[str] = None
    _length: int
    _words: List[str]

    def __init__(self, string: str = None):
        if string:
            self.string = string

    def __len__(self):
        return self._length

    def __call__(self, indx: int, *args, **kwargs):
        return self._words[indx]

    @property
    def string(self) -> Optional[str]:
        return self._string

    @string.setter
    def string(self, string: str):
        self._string = string
        words = string.split()
        self._words = words
        self._length = len(words)



