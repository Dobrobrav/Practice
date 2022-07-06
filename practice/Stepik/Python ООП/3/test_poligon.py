from CODE_3_3_7 import *

if __name__ == '__main__':
    # vector = RadiusVector(*(i for i in range(100_000)))
    vector = RadiusVector()
    vector.set_coords(3)
    vector.set_coords()
    a, b, c = vector.get_coords()
    print(a, b, c)
