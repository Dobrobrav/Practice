from typing import Dict


class RetrieveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')


# здесь объявляйте класс GeneralView
class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request: Dict[str, str]):
        self._is_allowed(request)
        method_request = request['method'].lower()
        return self.__getattribute__(method_request)(request)

    def _is_allowed(self, request: Dict[str, str]):
        if not request['method'] in self.allowed_methods:
            raise TypeError(f"Метод {request.get('method')} не разрешен.")


class DetailView(RetrieveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'POST')


if __name__ == '__main__':
    view = DetailView()
    html = view.render_request({'url': 'https://stepik.org/course/116336/',
                                'method': 'POST'})
    print(html)
