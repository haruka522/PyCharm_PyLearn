
# from functions import get_todos, write_todos
import functions2

from myfolder import something

user_prompt = (
    "Type add --thing to do-- or edit, complete with number of todo or exit: " + "\n"
)

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
            todos = functions2.get_todos()
            todos.append(todo)
            functions2.write_todos(todos)
        except FileNotFoundError:
            functions2.write_todos(todo)

    elif user_input.startswith("show"):
        todos = functions2.get_todos()
        for index, item in enumerate([item.strip("\n") for item in todos]):
            row = f"{index + 1}-{item}"
            print(row)

    elif user_input.startswith("edit"):
        try:
            edit_todo = user_input[5:].strip()
            edit_todo = int(edit_todo) - 1

            todos = functions2.get_todos()
            new_todo = input("Enter new todo: ").capitalize().strip()
            todos[edit_todo] = new_todo + "\n"

            functions2.write_todos(todos)
            print("Todo was edited successfully")

        except ValueError:
            print("Your command is not valid")
        except IndexError:
            print("There is no todo with that number")

    elif user_input.startswith("complete"):
        try:
            done_todo = user_input[9:].strip()
            done_todo = int(done_todo) - 1

            todos = functions2.get_todos()
            remove_todo = todos[done_todo].strip("\n")
            todos.pop(done_todo)

            functions2.write_todos(todos)
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
