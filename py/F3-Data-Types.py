# Data Types

# 1.Integers - int


from tkinter import Y


numbers = 2
print(numbers+2)


# 2.Floating Point - float
deciValue = 2.0
print(type(deciValue))

# 3.Strings - str
name = "Vinay"
print(name, type(name), type("Vinay"))

# 4.Lists - list
x = ["apple", "banana", "cherry"]
print(x)

# 5.Dictionaries- dict
dic = {"name": "John", "age": 36}
print(dic)

# 6.Tuples - tup
z = ("apple", "banana", "cherry")
print(z)

# 7.Sets - set
setA = {"apple", "banana", "cherry"}
print(setA)

# 8.Boolean - bool
bValue = False
bValue2 = True
print(type(bValue), bValue2)

# other ways to define

x1 = str("Hello World")
x2 = int(20)
x3 = float(20.5)
x4 = complex(1j)
x5 = list(("apple", "banana", "cherry"))
x6 = tuple(("apple", "banana", "cherry"))
x7 = range(6)
x8 = dict(name="John", age=36)
x9 = set(("apple", "banana", "cherry"))
x10 = frozenset(("apple", "banana", "cherry"))
x11 = bool(5)
x12 = bytes(5)
x13 = bytearray(5)
x14 = memoryview(bytes(5))
y = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14]
print(y)

# ['Hello World', 20, 20.5, 1j, ['apple', 'banana', 'cherry'], ('apple', 'banana', 'cherry'), 
# range(0, 6), {'name': 'John', 'age': 36}, {'banana', 'apple', 'cherry'}, frozenset({'banana', 'apple', 'cherry'}), 
# True, b'\x00\x00\x00\x00\x00', bytearray(b'\x00\x00\x00\x00\x00'), <memory at 0x10aa8a440>]