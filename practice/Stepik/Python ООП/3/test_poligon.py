from CODE_3_2_8 import *


if __name__ == '__main__':
    @Handler(methods=('GET', 'POST'))  # по умолчанию methods = ('GET',)
    def contact(request):
        return "Сергей Балакирев"

    print(contact({"method": "POST"}))
