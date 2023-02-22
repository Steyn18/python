num = 10
num = 20
num = num+num
print(num)
# 40


int = 40
float = 0.5
print(int, float)
# we can also assign a value to reserved keywords, but never use this keywords as variables

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x,y,z)
# apple banana cherry
print(x+y+z)
# applebananacherry

# --------------------------------------
# cant combine both int and str
# print(z+num)
# TypeError: can only concatenate str (not "int") to str



print(num+int)
#80