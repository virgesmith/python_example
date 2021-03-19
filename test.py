import python_example

#print(dir(python_example))
assert python_example.__version__

a = python_example.add(1,1) # C++
assert a == 2

b = python_example.py.mul(a, 3) # python
assert b == 6

b = python_example.mul(a, 3) # python
assert b == 6

