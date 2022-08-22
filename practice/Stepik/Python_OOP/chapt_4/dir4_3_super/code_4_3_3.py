class Book:
    title: str
    author: str
    pages: int
    year: int

    def __init__(self, title: str, author: str, pages: int, year: int):
        self.year = year
        self.pages = pages
        self.author = author
        self.title = title


class DigitBook(Book):
    size: int
    frm: str

    def __init__(self, title: str, author: str, pages: int,
                 year: int, size: int, frm: str):
        super(DigitBook, self).__init__(title, author, pages, year)
        self. size = size
        self.frm = frm


