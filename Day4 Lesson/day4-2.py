
a = input("Enter a number: ")
print(a, " Type of a is ", type(a))

b = int(a)
print(b, " Type of b is ", type(b))

print("a * b = ", a * b)
print()

# a is string, so a * 3 will be aaa and type of a * 3 is string
print(a * 3, " Type of a * 3 is ", type(a * 3))

# b is int, so b * 3 will be number of b*3 and type of b * 3 is int
print(b * 3, " Type of b * 3 is ", type(b * 3))
print()

x = 5.4

print(x, " type of x is ", type(x))
# x is float, so x * 3 will be float and type of x * 3 is float
print(x * 3, " type of x * 3 is ", type(x * 3))

# can also change string to interger or float by using int() or float()
print(int(x), " type of int(x) is ", type(int(x)))
print(float(b), " type of float(b) is ", type(float(b)))

print()

# can also change interger or float to string by using str()
print(type(str(b)), type(str(x)))

print()

# a is string, so a == b will be False and type of a == b is boolean
print(a == b, " type of a == b is ", type(a == b))

print(int(a) == b, " type of int(a) == b is ", type(int(a) == b))