FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of to-do items."""
    with open(filepath, "r") as file:
        y = file.readlines()
    return y


def write_todos(x, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(x)



if __name__ == "__main__":
    print("Hello World!!!")