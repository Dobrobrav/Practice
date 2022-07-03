from typing import Callable, Mapping, Optional


class HandlerGET:
    def __init__(self, func: Callable[[Mapping], str]):
        self._func = func

    def __call__(self, request: Mapping) -> Optional[str]:
        method = request.get("method", "GET")
        if method == "GET":
            return self.get(request)
        return None

    def get(self, request: Mapping, *args, **kwargs) -> str:
        return f"GET: {self._func(request)}"
