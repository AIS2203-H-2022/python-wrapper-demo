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

    del m


if __name__ == "__main__":
    main()
