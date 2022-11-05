class Book:
    _title: str
    _author: str
    _pages: int

    def __init__(self, title: str, author: str, pages: int):
        self._title = title
        self._author = author
        self._pages = pages

    def __str__(self):
        return f"Книга: {self._title}; {self._author}; {self._pages}"


if __name__ == '__main__':
    lst_in = [input() for _ in range(3)]
    book = Book(*lst_in)

    print(book)
