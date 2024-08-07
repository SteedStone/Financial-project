from cx_Freeze import setup, Executable
import sys
import os

# Define the base as "Win32GUI" for GUI applications
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# Define the paths to additional files
include_files = [
    ('path/to/file1', 'dest/path/in/exe'),
    ('path/to/file2', 'dest/path/in/exe'),
    # Add more files as needed
]

setup(
    name = "MyApp",
    version = "0.1",
    description = "My GUI application",
    options = {
        'build_exe': {
            'packages': [],  # Add any packages you need to include
            'include_files': include_files
        }
    },
    executables = [Executable("main.py", base=base)]
)
