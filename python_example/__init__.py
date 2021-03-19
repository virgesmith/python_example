
from _cpp_example import *
from . import pyimpl  as py # imported as python_example.py.{mul,div}
from .pyimpl import mul, div # imported as python_example.{mul,div}
__version__ = version_string # cant access _cpp_example.__version__ from here
