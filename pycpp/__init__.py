from __future__ import annotations

import platform
from ctypes import CDLL, Structure, POINTER, c_void_p, c_float


class Vector3(Structure):
    _fields_ = [("x", c_float), ("y", c_float), ("z", c_float)]

    def add(self, other: Vector3) -> Vector3:
        return CppLib()._vector3_add(self, other)

    def sub(self, other: Vector3) -> Vector3:
        return CppLib()._vector3_sub(self, other)

    def div(self, other: Vector3) -> Vector3:
        return CppLib()._vector3_div(self, other)

    def mul(self, other: Vector3) -> Vector3:
        return CppLib()._vector3_mul(self, other)

    def apply_matrix4(self, m: Matrix4) -> Vector3:
        return CppLib()._vector3_apply_matrix4(self, m._ptr)

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

    def make_rotation_x(self, theta: float):
        CppLib()._matrix4_make_rotation_x(self._ptr, theta)
        return self

    def make_rotation_y(self, theta: float):
        CppLib()._matrix4_make_rotation_y(self._ptr, theta)
        return self

    def make_rotation_z(self, theta: float):
        CppLib()._matrix4_make_rotation_z(self._ptr, theta)
        return self

    def copy(self, other: Matrix4):
        CppLib()._matrix4_copy(self._ptr, other._ptr)
        return self

    def __repr__(self):
        data = CppLib()._matrix4_data(self._ptr)
        return f"Matrix4({data[0]}, {data[4]}, {data[8]}, {data[12]}\n" \
               f"{data[1]}, {data[5]}, {data[9]}, {data[13]}\n" \
               f"{data[2]}, {data[7]}, {data[10]}, {data[14]}\n" \
               f"{data[3]}, {data[7]}, {data[11]}, {data[15]})"

    def __del__(self):
        CppLib()._matrix4_destroy(self._ptr)


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

        self._vector3_apply_matrix4 = self._handle.vector3_apply_matrix4
        self._vector3_apply_matrix4.argtypes = [Vector3, c_void_p]
        self._vector3_apply_matrix4.restype = Vector3

        self._matrix4_create = self._handle.matrix4_create
        self._matrix4_create.restype = c_void_p

        self._matrix4_identity = self._handle.matrix4_identity
        self._matrix4_identity.argtypes = [c_void_p]

        self._matrix4_set_position = self._handle.matrix4_set_position
        self._matrix4_set_position.argtypes = [c_void_p, c_float, c_float, c_float]

        self._matrix4_make_rotation_x = self._handle.matrix4_make_rotation_x
        self._matrix4_make_rotation_x.argtypes = [c_void_p, c_float]

        self._matrix4_make_rotation_y = self._handle.matrix4_make_rotation_y
        self._matrix4_make_rotation_y.argtypes = [c_void_p, c_float]

        self._matrix4_make_rotation_z = self._handle.matrix4_make_rotation_z
        self._matrix4_make_rotation_z.argtypes = [c_void_p, c_float]

        self._matrix4_copy = self._handle.matrix4_copy
        self._matrix4_copy.argtypes = [c_void_p, c_void_p]

        self._matrix4_data = self._handle.matrix4_data
        self._matrix4_data.argtypes = [c_void_p]
        self._matrix4_data.restype = POINTER(c_float)

        self._matrix4_destroy = self._handle.matrix4_destroy
        self._matrix4_destroy.argtypes = [c_void_p]


def CppLib():
    if _CppLib._instance is None:
        _CppLib._instance = _CppLib()
    return _CppLib._instance
