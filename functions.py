import os

FILEPATH = "todos.txt"

if not os.path.exists(FILEPATH):
    with open("todos.txt", "w") as file:
        pass


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """

    with open(filepath, "r") as file_local:
        return file_local.readlines()


def write_todos(value, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, "w") as file_local:
        file_local.writelines(value)
