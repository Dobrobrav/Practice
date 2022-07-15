from dir3_4_add_sub_mul_truediv.CODE_3_4_10 import *

if __name__ == '__main__':
    mp = MaxPooling(step=(2, 2), size=(2, 2))
    # res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])  # [[6, 8], [9, 7]]
    res = mp([
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]
    ])
    print(res)
