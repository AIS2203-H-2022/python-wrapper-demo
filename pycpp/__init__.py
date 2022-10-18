from __future__ import annotations

import platform
from ctypes import CDLL, Structure, POINTER, c_void_p, c_float


class Vector3(Structure):
    _fields_ = [("x", c_float), ("y", c_float), ("z", c_float)]

    def add(self, other: Vector3) -> Vector3:
        return _CppLib()._vector3_add(self, other)

    def __repr__(self):
        return f"Vector3(x={self.x}, y={self.y}, z={self.z})"


class Matrix4:

    def __init__(self):
        self._ptr = CppLib()._matrix4_create()

    def identity(self) -> Matrix4:
        CppLib()._matrix4_identity(self._ptr)
        return self

    def set_position(self, x: float, y: float, z: float) -> Matrix4:
        CppLib()._matrix4_set_position(self._ptr, x, y, z)
        return self

    def __repr__(self):
        data = CppLib()._matrix4_data(self._ptr)
        return f"Matrix4({data[0]}, {data[4]}, {data[8]}, {data[12]}\n" \
               f"{data[1]}, {data[5]}, {data[9]}, {data[13]}\n" \
               f"{data[2]}, {data[7]}, {data[10]}, {data[14]}\n" \
               f"{data[3]}, {data[7]}, {data[11]}, {data[15]})"


class _CppLib:
    _instance = None

    def __init__(self):

        def prefix() -> str:
            if platform.system() == "Windows":
                return "Release/"
            elif platform.system() == "Linux":
                return "lib"
            else:  # Darwin
                return "lib"  # ?????

        def suffix() -> str:
            if platform.system() == "Windows":
                return ".dll"
            elif platform.system() == "Linux":
                return ".so"
            else:  # Darwin
                return ".dylib"

        self._handle = CDLL(f"{__file__}/../build/bin/{prefix()}vecmathc{suffix()}")

        self._vector3_add = self._handle.vector3_add
        self._vector3_add.argtypes = [Vector3, Vector3]
        self._vector3_add.restype = Vector3

        self._vector3_sub = self._handle.vector3_sub
        self._vector3_sub.argtypes = [Vector3, Vector3]
        self._vector3_sub.restype = Vector3

        self._vector3_div = self._handle.vector3_div
        self._vector3_div.argtypes = [Vector3, Vector3]
        self._vector3_div.restype = Vector3

        self._vector3_mul = self._handle.vector3_mul
        self._vector3_mul.argtypes = [Vector3, Vector3]
        self._vector3_mul.restype = Vector3

        self._matrix4_create = self._handle.matrix4_create
        self._matrix4_create.restype = c_void_p

        self._matrix4_identity = self._handle.matrix4_identity
        self._matrix4_identity.argtypes = [c_void_p]

        self._matrix4_set_position = self._handle.matrix4_set_position
        self._matrix4_set_position.argtypes = [c_void_p, c_float, c_float, c_float]

        self._matrix4_data = self._handle.matrix4_data
        self._matrix4_data.argtypes = [c_void_p]
        self._matrix4_data.restype = POINTER(c_float)


def CppLib():
    if _CppLib._instance is None:
        _CppLib._instance = _CppLib()
    return _CppLib._instance


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


if __name__ == "__main__":
    main()
