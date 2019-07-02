import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}
build_exe_options = {"packages": ["numpy", "pygame"], "include_files" : ["components", "states", "menu_helpers.py"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Mission21",
        version = "1.0",
        description = "Escape the gravity",
        options = {"build_exe": build_exe_options},
        executables = [Executable("Main.py", base=base)])
