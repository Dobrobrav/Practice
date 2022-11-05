from typing import Tuple, Optional, Any, Dict


class GenericView:
    methods: Tuple[str, ...]
    a = 5

    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    def __init__(self, methods: Tuple[str, ...] = ('GET',)):
        super().__init__(methods)

    def render_request(self, request: Dict[str, Any], method: str):
        self._check_if_method_allowed(method)
        render_with_method = getattr(self, method.lower())
        return render_with_method(request)

    def get(self, request: Dict[str, Any]):
        self._check_request(request)
        return f"url: {request['url']}"

    def _check_request(self, request: Dict[str, Any]):
        self._check_if_is_dict(request)
        self._check_if_contains_url(request)

    @staticmethod
    def _check_if_is_dict(value: dict):
        if not isinstance(value, dict):
            raise TypeError('request не является словарем')

    @staticmethod
    def _check_if_contains_url(request: Dict[str, Any]):
        if 'url' not in request:
            raise TypeError('request не содержит обязательного ключа url')

    def _check_if_method_allowed(self, method: str):
        if not method.upper() in self.methods:
            raise TypeError('данный запрос не может быть выполнен')


if __name__ == '__main__':
   dv = DetailView()
   html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')
   print(html)

