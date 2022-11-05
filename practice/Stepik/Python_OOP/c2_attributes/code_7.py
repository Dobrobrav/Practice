class ValidateString:
    """ String descriptor for validating"""

    min_length: int
    max_length: int

    def __init__(self, min_length: int, max_length: int):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string: str) -> bool:
        return (isinstance(string, str)
                and self.min_length <= len(string) <= self.max_length)


class StringValue:
    """ String validator """

    validator: ValidateString

    def __init__(self, validator: ValidateString = None):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner) -> str:
        return getattr(instance, self.name)

    # Try using pattern matching!!
    def __set__(self, instance, value):
        if self.validator:
            if self.validator.validate(value):
                setattr(instance, self.name, value)
        else:
            setattr(instance, self.name, value)


class RegisterForm:
    """ Web-form for registration """

    login = StringValue(validator=ValidateString(min_length=3, max_length=100))
    password = StringValue(validator=ValidateString(min_length=3, max_length=100))
    email = StringValue(validator=ValidateString(min_length=3, max_length=100))

    def __init__(self, login: str, password: str, email: str):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self) -> list:
        """ Return list of fields in the order [login, password, email] """

        return [self.login, self.password, self.email]

    def show(self) -> str:
        return (
            "<form>\n"
            f"Логин: {self.login}\n"
            f"Пароль: {self.password}\n"
            f"Email: {self.email}\n"
            "</form>"
        )


if __name__ == '__main__':
    form = RegisterForm("sok9@tpu.ru", "gqIuFxM2", "sok9@tpu.ru")
    print(form.__dict__)

    form = RegisterForm(1, "gqIuFxM2", "sok9@tpu.ru")
    print(form.__dict__)




