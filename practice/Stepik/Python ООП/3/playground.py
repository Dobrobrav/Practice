class Foo:
    def __eq__(self, other):
        return True


print(Foo.__name__)


foos = [Foo() for _ in range(10)]
print(foos.count(Foo()))
