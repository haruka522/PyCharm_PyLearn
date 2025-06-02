
text = "Hello World"
mylist = [1,2,3,4,5]


print(dir(str))
print()

# if you don't know the type of the object you can use type() method
print(type(text))
print(dir(text))
print()

# dir() method is used to get all the methods and attributes of an object
# usable methods are without double underscore

print(type(mylist))
print(dir(mylist))
print()

# if you don't know how to use a method you can use help() method
print(help(text.capitalize))

print(help(list.append))
# you will see that append need argument to work
print()


# if you want to see the builtin method like input or else you can do like this
print("Builtin methods: ")
import builtins
print(dir(builtins))
print()

print(help(input))

