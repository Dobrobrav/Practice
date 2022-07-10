from F3_4_add_sub_mul_truediv.CODE_3_4_4 import *

if __name__ == '__main__':
    lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
    lst2 = NewList([0, 1, 2, 3, True])
    res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
    lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
    res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
    res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
    a = NewList([2, 3])
    res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]

    lst = NewList()
    print(lst.get_list())
