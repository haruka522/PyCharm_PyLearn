def get_todos(filepath="todos.txt"):
    """Read a text file and return the list of to-do items."""
    with open(filepath, "r") as file:
        y = file.readlines()
    return y


def write_todos(x, filepath="todos.txt"):
    with open(filepath, "w") as file:
        file.writelines(x)