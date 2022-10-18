from __future__ import annotations

import platform
import numpy as np
from ctypes import CDLL, Structure, POINTER, c_void_p, c_float


class Vector3(Structure):
    _fields_ = [("x", c_float), ("y", c_float), ("z", c_float)]

    def add(self, other: Vector3) -> Vector3:
        return _CppLib().vector3_add(self, other)

    def __repr__(self):
        return f"Vector3(x={self.x}, y={self.y}, z={self.z})"


class Matrix4:

    def __init__(self):
        self._ptr = CppLib().matrix4_create()

    def identity(self) -> Matrix4:
        CppLib().matrix4_identity(self._ptr)
        return self

    def __repr__(self):
        data = CppLib().matrix4_data(self._ptr)
        return f"Matrix4({data[0]}, {data[1]}, {data[2]}, {data[3]}\n" \
               f"{data[4]}, {data[5]}, {data[6]}, {data[7]}\n" \
               f"{data[8]}, {data[9]}, {data[10]}, {data[11]}\n" \
               f"{data[12]}, {data[13]}, {data[14]}, {data[15]})"


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

        self.vector3_add = self._handle.vector3_add
        self.vector3_add.argtypes = [Vector3, Vector3]
        self.vector3_add.restype = Vector3

        self.vector3_sub = self._handle.vector3_sub
        self.vector3_sub.argtypes = [Vector3, Vector3]
        self.vector3_sub.restype = Vector3

        self.vector3_div = self._handle.vector3_div
        self.vector3_div.argtypes = [Vector3, Vector3]
        self.vector3_div.restype = Vector3

        self.vector3_mul = self._handle.vector3_mul
        self.vector3_mul.argtypes = [Vector3, Vector3]
        self.vector3_mul.restype = Vector3

        self.matrix4_create = self._handle.matrix4_create
        self.matrix4_create.restype = c_void_p

        self.matrix4_identity = self._handle.matrix4_identity
        self.matrix4_identity.argtypes = [c_void_p]

        self.matrix4_data = self._handle.matrix4_data
        self.matrix4_data.argtypes = [c_void_p]
        self.matrix4_data.restype = POINTER(c_float)


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


if __name__ == "__main__":
    main()
