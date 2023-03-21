from typing import Callable, Literal


class Request:
    method: str

    def __init__(self,
                 method: Literal['GET', 'POST']) -> None:
        self.method = method


class Response:
    res: str

    def __init__(self,
                 res: str) -> None:
        self.res = res


class View:
    @property
    def http_method_names(self):
        return list(self.FUNCTION_BY_METHOD.keys())
    
    def __init__(self,
                 *args, **initkwargs) -> None:
        self.args = args
        self.initkwargs = initkwargs
        self.FUNCTION_BY_METHOD = {
            'GET': self.get,
            'POST': self.post,
        }

    def __call__(self, request: Request,
                 *args, **kwargs) -> Response:
        ...
        return self.dispatch(request, *args, **kwargs)

    @classmethod
    def as_view(cls: type,
                *args, **initkwargs) -> Callable:
        return cls(**initkwargs)

    def dispatch(self, request: Request,
                 *args, **kwargs) -> Response:
        method_function = self.FUNCTION_BY_METHOD.get(
            request.method, default=self.http_method_not_allowed
        )
        return method_function(request, *args, **kwargs)

    def get(self,
            request: Request,
            *args, **kwargs) -> Response:
        return Response(res='GET response')

    def post(self,
             request: Request,
             *args, **kwargs) -> Response:
        return Response(res='POST response')

    def http_method_not_allowed(self, request: Request,
                                *args, **kwargs) -> Response:
        return Response(res=f'{request.method} method is not allowed')
