class Book:
    """ Class for describing individual books with title, author and year. """

    title: str
    author: str
    year: int

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year


class Lib:
    """ Class that represents libraries with books
     and allows to add and delete the books through '+' and '-', respectively.
     """

    book_list: list[Book]

    def __init__(self):
        self.book_list = []

    def __add__(self, other: Book) -> 'Lib':  # doesn't create new instance
        self.book_list.append(other)
        return self

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other: Book | int) -> 'Lib':  # doesn't create new instance
        if isinstance(other, int):
            self.book_list.pop(other)
        else:
            self.book_list.remove(other)
        return self

    def __isub__(self, other):
        return self - other

    def __len__(self):
        return len(self.book_list)


