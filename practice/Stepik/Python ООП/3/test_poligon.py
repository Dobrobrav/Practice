from dir3_4_add_sub_mul_truediv.CODE_3_4_10 import *

if __name__ == '__main__':
    mp = MaxPooling(step=(2, 2), size=(2, 2))
    print(mp._calc_area_max_value.__annotations__)
