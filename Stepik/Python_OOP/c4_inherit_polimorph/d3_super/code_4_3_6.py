from typing import Callable, Dict


class Router:
    app: Dict[str, Callable] = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func


# здесь объявляйте декоратор Callback
class Callback:
    _path: str
    _router_cls: type

    def __init__(self, path: str, router_cls: type):
        self.path = path
        self._router_cls = router_cls

    def __call__(self, func: Callable, *args, **kwargs):
        self._router_cls.add_callback(self.path, func)
        return self._router_cls.get(self.path)


@Callback('/', Router)
def index():
    return '<h1>Главная</h1>'
