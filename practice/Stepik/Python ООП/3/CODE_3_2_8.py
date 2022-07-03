from typing import Callable, Mapping, Optional, Dict, Sequence, TypeAlias


RequestFunc: TypeAlias = Callable[[Mapping], str]


class Handler:
    """
    Decorator with parameters (sequence of allowed types);
    return function for processing requests of allowed type.
    """
    _methods: Sequence
    _method_functions: Dict[str, Callable]

    def __init__(self, methods: Sequence = ("GET",)):
        self._methods = methods
        self._method_functions = {
            "GET": self.get,
            "POST": self.post,
        }

    def __call__(self, func: RequestFunc) -> Callable[[Mapping], Optional[str]]:
        """ Return function for processing requests. """
        def wrapper(request: Mapping) -> Optional[str]:
            method = request.get("method", "GET")
            if method in self._methods:
                return self._method_functions[method](func, request)
            return None

        return wrapper

    def get(self, func: RequestFunc, request: Mapping, *args, **kwargs) -> str:
        return f"GET: {func(request)}"

    def post(self, func: RequestFunc, request: Mapping, *args, **kwargs) -> str:
        return f"POST: {func(request)}"
