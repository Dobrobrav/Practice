class IterColumn:
    lst: list[list]
    column: int

    def __init__(self, lst: list[list], column: int):
        self.lst = lst
        self.column = column

    def __iter__(self):
        """ Iterate the typed column of the typed 2D-list. """
        for row in self.lst:
            yield row[self.column]
