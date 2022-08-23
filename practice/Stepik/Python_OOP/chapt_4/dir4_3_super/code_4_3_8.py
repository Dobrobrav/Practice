class SoftList(list):
    def __getitem__(self, item):
        try:
            return super(SoftList, self).__getitem__(item)
        except IndexError:
            return False
