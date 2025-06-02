
user_prompt = "Enter a todo: "
todos = []


# While loop will run till the condition is true until the user enters "exit"
while True:  # Changing True to False will stop the loop
    
    todo = input(user_prompt)
    
    todos.append(todo)
    # append method is to add the new value to the todos list
    # todos = [todo1, todo2, todo3, etc..]
    
    print(todos)
    
    # Check the data type of todos (List data type)
    print(type(todos), " Data Type of todos")
    
    # Check the length of todos (how many items in the list)
    print(len(todos), " length of todos")
    
    # Check the data type of user_prompt
    print(type(user_prompt), " Data Type of user_prompt")
    
    # Check the data type of todo
    print(type(todo), " Data Type of todo")
    
    print("Next...")
