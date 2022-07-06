class Foo:
    def __len__(self):
        return None


f = Foo()
print(len(f))  # len can only return integers!


