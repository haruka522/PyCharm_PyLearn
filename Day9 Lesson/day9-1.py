user_prompt = "Type add --thing to do-- or edit, complete with number of todo or exit: " +'\n'

while True:
    user_input = input(user_prompt)
    user_input = user_input.strip()

    # "if" is a conditional statement, if the condition is true, it will execute the code below and return true
    # if "add" in user_input: will check if the string "add" is in the user_input
    if "add" in user_input:
        # [:] is a slice operator, [start:end] , if start is not specified, it will start from the beginning, if end is not specified, it will go to the end
        todo = user_input[4:]
        todo = todo.capitalize().strip()
        with open("todos.txt", "r") as file:
            todos = file.readlines()
            todos.append(todo + "\n")
        with open("todos.txt", "w") as file:
            file.writelines(todos)

    if "show" in user_input:
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        for index, item in enumerate([item.strip("\n") for item in todos]):
            row = f"{index + 1}-{item}"
            print(row)

    if "edit" in user_input:
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        edit_todo = user_input[5:]
        edit_todo = edit_todo.strip()
        new_todo = input("Enter new todo: ").capitalize().strip()
        todos[int(edit_todo) - 1] = new_todo + "\n"

        with open("todos.txt", "w") as file:
            file.writelines(todos)
        print("Todo was edited successfully")

    if "complete" in user_input:
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        done_todo = user_input[9:]
        done_todo = done_todo.strip()
        remove_todo = todos[int(done_todo) - 1].strip("\n")
        todos.pop(int(done_todo) - 1)

        with open("todos.txt", "w") as file:
            file.writelines(todos)
        print(f"{remove_todo} was marked as complete")

    if "exit" in user_input:
        break

print("Bye!")
