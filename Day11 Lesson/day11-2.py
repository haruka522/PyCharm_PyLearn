user_prompt = (
    "Type add --thing to do-- or edit, complete with number of todo or exit: " + "\n"
)

# write functions to reduce code redundancy
def get_todos():
    with open("todos.txt", "r") as file:
        y = file.readlines()
    return y

def write_todos(x):
    with open("todos.txt", 'w') as file:
        file.writelines(x)

while True:
    user_input = input(user_prompt)
    user_input = user_input.strip()

    if user_input.startswith("add"):

        todo = user_input[4:]
        if todo == "":
            print("You didn't enter anything to add")
            continue
        todo = todo.capitalize().strip() + "\n"
        
        # to check if there is todos.txt file or not. if not, it will create todos.txt file 
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
