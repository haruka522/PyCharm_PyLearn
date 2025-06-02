user_prompt = "Type add, show, edit, complete or exit: "

while True:
    user_input = input(user_prompt)
    user_input = user_input.strip()
    match user_input:
        case "add":
            todo = input("Enter a todo: ")
            todo = todo.capitalize().strip()

            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()
            todos.append(todo + "\n")
            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()

        case "show":
            # just some other ways to show todos list to user, nothing serious.

            # Method 1
            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()
            # for index, item in enumerate(todos):
            #     item = item.strip('\n')
            #     row = f"{index + 1}-{item}"
            #     print(row)

            # Method 2
            # show_todos = []
            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()
            # for item in todos:
            #     item = item.strip('\n')
            #     show_todos.append(item)
            # for index, item in enumerate(show_todos):
            #     row = f"{index + 1}-{item}"
            #     print(row)

            # Method 3
            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()
            # show_todos = [item.strip('\n') for item in todos]
            # for index, item in enumerate(show_todos):
            #     row = f"{index + 1}-{item}"
            #     print(row)

            # Method 4
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            for index, item in enumerate([item.strip("\n") for item in todos]):
                row = f"{index + 1}-{item}"
                print(row)

        case "edit":
            # same as show, literally just to show user the number of todos, so the user will know which todo to edit
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}-{item}"
                print(row)

            edit_todo = input("Enter the number of the todo to edit: ")
            edit_todo = edit_todo.strip()
            new_todo = input("Enter new todo: ").capitalize().strip()
            todos[int(edit_todo) - 1] = new_todo + "\n"

            # write the new edited todo to the file
            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()
            print("Todo was edited successfully")

        case "complete":
            # same as show, literally just to show user the number of todos, so the user will know which todo to complete
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}-{item}"
                print(row)

            # get the number of todo to complete from the user and reemove it from the list
            done_todo = input("Enter the number of the todo to complete: ")
            done_todo = done_todo.strip()
            remove_todo = todos[int(done_todo) - 1].strip("\n")
            todos.pop(int(done_todo) - 1)

            # write the new list of todos to the file
            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()
            print(f"{remove_todo} was marked as complete")

        case "exit":
            break
        case _:
            print("Unknown command")

print("Bye!")
