user_prompt = (
    "Type add --thing to do-- or edit, complete with number of todo or exit: " + "\n"
)

while True:
    user_input = input(user_prompt)
    user_input = user_input.strip()

    # startswith() is a method that returns true if the string starts with the specified value, if not it will return false
    if user_input.startswith("add"):

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

    elif user_input.startswith("show"):
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        for index, item in enumerate([item.strip("\n") for item in todos]):
            row = f"{index + 1}-{item}"
            print(row)

    elif user_input.startswith("edit"):
        try:
            edit_todo = user_input[5:].strip()
            edit_todo = int(edit_todo) - 1
            
            # read the file here cuz if the user_input check fails, it will not read the file and go to the except block
            # so it will speed up the process. Only for ValueError and not for IndexError
            # for IndexError, it will need to read the file to check if the index is valid
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            new_todo = input("Enter new todo: ").capitalize().strip()
            todos[edit_todo] = new_todo + "\n"

            with open("todos.txt", "w") as file:
                file.writelines(todos)
            print("Todo was edited successfully")
            
        # if you want to use multiple exceptions in one line, you can use a tuple
        # except (ValueError, IndexError):
        #     print("Your command is not valid")
        except ValueError:
            print("Your command is not valid")
        except IndexError:
            print("There is no todo with that number")

            
    elif user_input.startswith("complete"):
        try:
            done_todo = user_input[9:].strip()
            done_todo = int(done_todo) - 1
            
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            remove_todo = todos[done_todo].strip("\n")
            todos.pop(done_todo)

            with open("todos.txt", "w") as file:
                file.writelines(todos)
            print(f"{remove_todo} was marked as complete")
        except ValueError:
            print("Your command is not valid")
        except IndexError:
            print("There is no todo with that number")

    elif "exit" in user_input:
        break

    else:
        print("Unknown command")

print("Bye!")
