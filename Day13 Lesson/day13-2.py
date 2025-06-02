user_prompt = (
    "Type add --thing to do-- or edit, complete with number of todo or exit: " + "\n"
)


def get_todos(filepath="todos.txt"):
    # to add documentation to a function, use triple quotes
    """Read a text file and return the list of to-do items."""
    with open(filepath, "r") as file:
        y = file.readlines()
    return y


def write_todos(x, filepath="todos.txt"):
    with open(filepath, "w") as file:
        file.writelines(x)


# to read the documentation of a function, use help()
# print(help(get_todos))

while True:
    user_input = input(user_prompt)
    user_input = user_input.strip()

    if user_input.startswith("add"):

        todo = user_input[4:]
        if todo == "":
            print("You didn't enter anything to add")
            continue
        todo = todo.capitalize().strip() + "\n"

        try:
            todos = get_todos()
            todos.append(todo)
            write_todos(todos)
        except FileNotFoundError:
            write_todos(todo)

    elif user_input.startswith("show"):
        todos = get_todos()
        for index, item in enumerate([item.strip("\n") for item in todos]):
            row = f"{index + 1}-{item}"
            print(row)

    elif user_input.startswith("edit"):
        try:
            edit_todo = user_input[5:].strip()
            edit_todo = int(edit_todo) - 1

            todos = get_todos()
            new_todo = input("Enter new todo: ").capitalize().strip()
            todos[edit_todo] = new_todo + "\n"

            write_todos(todos)
            print("Todo was edited successfully")

        except ValueError:
            print("Your command is not valid")
        except IndexError:
            print("There is no todo with that number")

    elif user_input.startswith("complete"):
        try:
            done_todo = user_input[9:].strip()
            done_todo = int(done_todo) - 1

            todos = get_todos()
            remove_todo = todos[done_todo].strip("\n")
            todos.pop(done_todo)

            write_todos(todos)
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
