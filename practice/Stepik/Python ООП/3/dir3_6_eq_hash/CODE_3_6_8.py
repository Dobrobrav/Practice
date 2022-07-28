class BookStudy:
    """ Class that represents a study book with name, author and year.
    Books with the same name and author have the same hash
     and are considered equal.
    """

    name: str
    author: str
    year: int

    def __init__(self, name: str, author: str, year: int):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other: object):
        if not isinstance(other, BookStudy):
            return NotImplemented
        return hash(self) == hash(other)

    def __repr__(self):
        return f"{self.name}-{self.author}"


if __name__ == '__main__':
    lst_in = [
        'Python; Балакирев С.М.; 2020',
        'Python ООП; Балакирев С.М.; 2021',
        'Python ООП; Балакирев С.М.; 2022',
        'Python; Балакирев С.М.; 2021',
    ]

    lst_bs = [BookStudy(split_line[0], split_line[1], int(split_line[2]))
              for line in lst_in
              for split_line in (line.split('; '),)]

    unique_books = len(set(lst_bs))

    print(unique_books)
