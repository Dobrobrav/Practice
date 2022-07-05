class Foo:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f"Foo: {self.a}"

    def __repr__(self):
        return f"REPR: {self.a}"


lst = [Foo(i) for i in range(10)]
print(lst)
print(lst[1])



