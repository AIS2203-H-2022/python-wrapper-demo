import math
from pycpp import Vector3, Matrix4


def main():
    v1 = Vector3(1, 2, 3)
    v2 = Vector3(1, 1, 1)
    res = v1.add(v2)
    print(res)

    m = Matrix4()
    m.identity()
    print(m)
    m.set_position(10, -5, 6)
    print(m)

    m.make_rotation_y(math.radians(90))
    rotated = v1.apply_matrix4(m)
    print(rotated)

    del m


if __name__ == "__main__":
    main()
