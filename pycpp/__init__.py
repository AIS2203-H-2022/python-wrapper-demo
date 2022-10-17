
import platform
from ctypes import CDLL

class _CppLib:
    _instance = None

    def __init__(self):

        def prefix() -> str:
            if platform.system() == "Windows":
                return ""
            elif platform.system() == "Linux":
                return "lib"
            else:  # Darwin
                return "lib" # ?????

        def suffix() -> str:
            if platform.system() == "Windows":
                return ".dll"
            elif platform.system() == "Linux":
                return ".so"
            else:  # Darwin
                return ".dylib"

        self._handle = CDLL(f"{__file__}/../build/bin/{prefix()}person{suffix()}")



def CppLib():
    if _CppLib._instance is None:
        _CppLib._instance = _CppLib()
    return _CppLib._instance
