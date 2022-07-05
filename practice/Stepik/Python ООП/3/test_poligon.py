from CODE_3_3_5 import *


if __name__ == '__main__':
    linked_lst = LinkedList()
    linked_lst.add_obj(ObjList("Sergey"))
    linked_lst.add_obj(ObjList("Balakirev"))
    linked_lst.add_obj(ObjList("Python"))
    linked_lst.add_obj(ObjList("Python ООП"))
    n = len(linked_lst)  # n = 3
    s = linked_lst(1)  # s = Balakirev

    for i in range(4):
        print(linked_lst(i))
    print()

    for i in range(-1, -5, -1):
        print(linked_lst(i))
