import sys
from cx_Freeze import setup, Executable
import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["pkg_resources","asyncio","os","pandas","numpy","idna","folium","branca","jinja2","matplotlib","seaborn.cm","geopandas","PyQt5.QtWebEngineWidgets"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

options = {
    'build_exe': {
        'include_files':[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
            # 'C:\\Users\\natha\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\branca\\_cnames.json',
            # 'C:\\Users\\natha\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\branca\\_schemes.json'
         ],
    },
}

setup(  name = "MyProgram",
        version = "0.1",
        description = "MyProgram that I created",
        options = {"build_exe": build_exe_options},
        executables = [Executable("CovidTrackingApp.py", base=base)])