class Num:
    def __init__(self, num: int):
        self.num = num

    def __add__(self, other: int):
        return self.num + other


num = Num(15)

print(15 + num)