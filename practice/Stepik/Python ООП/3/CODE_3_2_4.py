from string import ascii_lowercase, digits


class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True


# здесь прописывайте классы валидаторов: LengthValidator и CharsValidator
class LengthValidator:
    """ Functor that validates length of strings """

    _min_length: int
    _max_length: int

    def __init__(self, min_length: int, max_length: int):
        self._min_length = min_length
        self._max_length = max_length

    def __call__(self, string: str, *args, **kwargs) -> bool:
        return self._min_length <= len(string) <= self._max_length


class CharsValidator:
    """ Functor that validates strings for chars it consists of """

    _chars: str

    def __init__(self, chars: str):
        self._chars = chars

    def __call__(self, string, *args, **kwargs) -> bool:
        return all(char in self._chars for char in string)
