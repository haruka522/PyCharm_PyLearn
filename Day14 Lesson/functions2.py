def get_todos(filepath="todos.txt"):
    """Read a text file and return the list of to-do items."""
    with open(filepath, "r") as file:
        y = file.readlines()
    return y


def write_todos(x, filepath="todos.txt"):
    with open(filepath, "w") as file:
        file.writelines(x)
        

print("Hello from functions2.py")


print(__name__)


# if we run functions2.py, __name__ will be __main__,
# if we import functions2.py and run it from another file, __name__ will be functions2
# so we can use this to check if we are running the file or importing it
if __name__ == "__main__":
    print("Hello World!!!")

