user_prompt = "Type add, show, edit, complete or exit: "

while True:
    user_input = input(user_prompt)
    user_input = user_input.strip()
    match user_input:
        case "add":
            todo = input("Enter a todo: ")
            todo = todo.capitalize().strip()

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            todos.append(todo + "\n")
            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)

        case "show":
            
            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()
            
            # this is the same as the above 3 lines but more efficient and don't need to close the file
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            
            for index, item in enumerate([item.strip("\n") for item in todos]):
                row = f"{index + 1}-{item}"
                print(row)

        case "edit":
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}-{item}"
                print(row)

            edit_todo = input("Enter the number of the todo to edit: ")
            edit_todo = edit_todo.strip()
            new_todo = input("Enter new todo: ").capitalize().strip()
            todos[int(edit_todo) - 1] = new_todo + "\n"

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            print("Todo was edited successfully")

        case "complete":
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}-{item}"
                print(row)

            done_todo = input("Enter the number of the todo to complete: ")
            done_todo = done_todo.strip()
            remove_todo = todos[int(done_todo) - 1].strip("\n")
            todos.pop(int(done_todo) - 1)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            print(f"{remove_todo} was marked as complete")

        case "exit":
            break
        case _:
            print("Unknown command")

print("Bye!")
