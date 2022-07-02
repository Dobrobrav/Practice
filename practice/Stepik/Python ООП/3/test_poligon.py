from CODE_3_2_6 import *

if __name__ == '__main__':
    lst = ["Пункт меню 1", "sdlfkj", "Пункт меню 2", "Пункт меню 3"]
    render = RenderList("ll")
    html = render(lst)
    print(html)
