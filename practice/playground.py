def main():
    x = X(10)
    y = Y(10)
    z = Z(5)

    print(x == 10 or y == 15 and z == 6)


class X:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        print("X working")
        return self.value == other


class Z:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        print("Z working")
        return self.value == other


class Y:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        print("Y working")
        return self.value == other


if __name__ == '__main__':
    main()
