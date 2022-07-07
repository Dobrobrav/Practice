from F3_3_STR_REPR_LEN_ABS.CODE_3_3_8 import *

if __name__ == '__main__':
    dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
    print(dt)  # 01: 30: 00
    len_dt = len(dt)  # 5400
    print(f"{len_dt = }")
