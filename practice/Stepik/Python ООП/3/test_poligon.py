from CODE_3_2_7 import *

if __name__ == '__main__':
    @HandlerGET
    def contact(request):
        return "Сергей Балакирев"


    res = contact({"method": "GET", "url": "contact.html"})

    print(res)
