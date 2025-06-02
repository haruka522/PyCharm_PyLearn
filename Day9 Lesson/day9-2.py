user_prompt = (
    "Type add --thing to do-- or edit, complete with number of todo or exit: " + "\n"
)

while True:
    user_input = input(user_prompt)
    user_input = user_input.strip()

    # "not in" is a conditional statement, if the condition is false, it will execute the code below and return true. oppsite to "in"
    if "add" in user_input:

        todo = user_input[4:]
        if todo == "":
            print("You didn't enter anything to add")
            continue
        todo = todo.capitalize().strip()
        with open("todos.txt", "r") as file:
            todos = file.readlines()
            todos.append(todo + "\n")
        with open("todos.txt", "w") as file:
            file.writelines(todos)

    # use elif instead of if to optimize the code, so that it will not check the other conditions if the first condition is met
    elif "show" in user_input:
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        for index, item in enumerate([item.strip("\n") for item in todos]):
            row = f"{index + 1}-{item}"
            print(row)

    elif "edit" in user_input:

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        edit_todo = user_input[5:].strip()
        
        # check if the user did not enter a number or an empty string
        # or operator returns true if both or one of the conditions is true, 
        # and operator returns true if both of the conditions is true, if not it will return false
        # isdigit() is a method that returns true if the string is a number, if not it will return false
        
        if edit_todo == "" or edit_todo.isdigit() == False:
            print("You did not enter a number of to do to edit")
            # continue is used to skip the rest of the code in the loop and go to start of the loop again
            continue
        new_todo = input("Enter new todo: ").capitalize().strip()
        todos[int(edit_todo) - 1] = new_todo + "\n"

        with open("todos.txt", "w") as file:
            file.writelines(todos)
        print("Todo was edited successfully")

    elif "complete" in user_input:

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        done_todo = user_input[9:].strip()
        if done_todo == "" or done_todo.isdigit() == False:
            print("You did not enter a number of to do to complete")
            continue
        remove_todo = todos[int(done_todo) - 1].strip("\n")
        todos.pop(int(done_todo) - 1)

        with open("todos.txt", "w") as file:
            file.writelines(todos)
        print(f"{remove_todo} was marked as complete")

    elif "exit" in user_input:
        break

    # if all the conditions are not met, then the else statement will be executed
    else:
        print("Unknown command")

print("Bye!")
