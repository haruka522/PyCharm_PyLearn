import pathlib

FILEPATH = pathlib.Path("Day19 Lesson", "todos.txt")

def get_todos(filepath=FILEPATH):
    try:
        with open(filepath, "r") as file:
            y = file.readlines()
    except FileNotFoundError:
        # Create the file if it doesn't exist, then read (will be empty)
        with open(filepath, "w") as file:
            # pass is just a placeholder, it doesn't do anything
            pass
        y = []
    return y


def write_todos(x, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(x)



if __name__ == "__main__":
    print("Hello World!!!")