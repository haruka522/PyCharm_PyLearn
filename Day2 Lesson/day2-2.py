
# user_prompt = "Enter a todo: "

# while True:
    
#     todo = input(user_prompt)
    
#     # without appending to the list, todos list will be overwritten every time
#     # also todos list need to be defined before the while loop
    
#     todos = [todo]
    
#     print(todos)


user_prompt = "Enter a todo: "
todos = []

while True:

    todo = input(user_prompt)
    
    # this will only capitalize the first letter of the todo but not the rest of the value
    todo.capitalize()
    print(todo)

    # this will capitalize the first letter of the todo and the rest of the value
    todo = todo.capitalize()
    print(todo)
    
    todos.append(todo)
    print(todos)

    print("Next...")
    

# in todo.capitalize() the .capitalize() is a method of the string data type
# methods are functions that are built into the data type but not the same as functions
# methods can also take arguments like functions
# methods usually follow with a dot after the variable name