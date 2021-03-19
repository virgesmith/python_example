from setuptools import setup, find_packages

# attempting a mixed python-C++ package

# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension

import sys

__version__ = "0.0.1"

# The main interface is through Pybind11Extension.
# * You can add cxx_std=11/14/17, and then build_ext can be removed.
# * You can set include_pybind11=false to add the include directory yourself,
#   say from a submodule.
#
# Note:
#   Sort input source files if you glob sources to ensure bit-for-bit
#   reproducible builds (https://github.com/pybind/python_example/pull/53)

ext_modules = [
    Pybind11Extension("_cpp_example",
        ["src/main.cpp"],
        # Example: passing in the version to the compiled code
        define_macros = [('VERSION_INFO', __version__)],
        cxx_std=17
        ),
]

setup(
    name="python_example",
    version=__version__,
    url="https://github.com/virgesmith/python_example",
    description="A test mixed python and C++ project using pybind11, based on https://github.com/pybind/python_example",
    long_description="",
    packages = find_packages(),
    ext_modules=ext_modules,
    extras_require={"test": "pytest"},
    zip_safe=False,
)
