# in Python, function start with def and then we write its name, and then we put a colon

def greet():
    message = "hello"
    new_message = message.capitalize()
    # need to return if the function is gonna assign in a variable. the return value will be assigned in the variable
    return new_message

def greet2():
    message = "hello2"
    print(message.capitalize())
    

# need a parameter in (), cuz there is something to with that parameter in the function
# don't need to return if the function will do its job and has nothing to do after that
def greet3(name):
    message = "hello3" + str(name)
    print(message.capitalize())

def greet4(name):
    message = "hello4" + str(name)
    return message.capitalize()


# need to call the function to run it, if not, it will not run


# this will not print anything
# greet()

# this will print the Hello
hi = greet()
print(hi)

print()

# this will print the Hello2, don't need to assign to a variable
greet2()

print()

# this will throw an error, cuz this function need a parameter to run properly
# greet3()

# this will print the Hello3Smith
greet3("Smith")

print()

# this will print nothing
greet4("Allen")

# this will print the Hello4Allen
hi4 = greet4("Allen")
print(hi4)


# Variable Scope
# Variable inside a function is local, and variable outside a function is global
# local variable can only be used inside the function, can't be used outside the function, that's why we need to return the value from the function
# global variable can be used anywhere
# if we want to declare a global variable inside a function, we need to use the global keyword before the variable name, like this: global var_name
