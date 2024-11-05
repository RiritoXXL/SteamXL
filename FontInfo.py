import os
import pathlib
import ctypes
def get_FontDir_bool() -> ctypes.c_bool:
    fontdirandfile = pathlib.Path(str(os.getcwd() + "\\Font\\SourceCodePro.ttf")).is_file()
    if(fontdirandfile == ctypes.c_bool(False)):
        return ctypes.c_bool(False)
    else:
        return ctypes.c_bool(True)

def FontDir_String() -> str:
    return str(os.getcwd() + "\\Font\\SourceCodePro.ttf")