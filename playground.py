def main():
    foo = Foo()
    foo.fuck()


class Foo:
    @classmethod
    def fuck(cls):
        print("fuck")


if __name__ == '__main__':
    main()
