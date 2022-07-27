class Record:
    """ Class that represents records in DB.

    The record contains attrs:
     - pk - primary key
     - fio - first name, second name, middle name
     - old

    All records with the same fio (case-insensitive) and old
    have the same hash and are considered equal ('==' operation).
    """

    start_pk = 1
    pk: int
    fio: str
    descr: str
    old: int

    def __init__(self, fio: str, descr: str, old: int):
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = self.start_pk
        self.__class__.start_pk += 1

    def __repr__(self):
        return f"{self.fio}, {self.descr}, {self.pk}"

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Record):
            return NotImplemented
        return hash(self) == hash(other)


class DataBase:
    """ Class that represents a database.

    The DB has attrs:
     - path
     - dict_db - dictionary that associates all the same
       (regarding fio and old) records (Record class) together.

    Class implements methods:
     - .write - add a record to the dict
     - .read - get the record by its pk
    """

    path: str
    dict_db: dict[Record, list[Record]]

    def __init__(self, path: str):
        self.path = path
        self.dict_db = {}

    def __repr__(self):
        return self.path

    def write(self, record: Record):
        if record not in self.dict_db:
            self.dict_db[record] = [record]
        else:
            self.dict_db[record].append(record)

    def read(self, pk: int) -> Record | None:
        for record_list in self.dict_db.values():
            for record in record_list:
                if record.pk == pk:
                    return record

        return None


if __name__ == '__main__':
    lst_in = [
        'Балакирев С.М.; программист; 33',
        'Кузнецов Н.И.; разведчик - нелегал; 35',
        'Суворов А.В.; полководец; 42',
        'Иванов И.И.; фигурант всех подобных списков; 26',
        'Балакирев С.М.; преподаватель; 33',
    ]

    db = DataBase('abc')
    for line in lst_in:
        fio, descr, old = line.split('; ')
        db.write(Record(fio, descr, int(old)))

    print(db.dict_db)
