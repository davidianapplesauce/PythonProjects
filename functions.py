FILEPATH= "todos.txt" # this is the default value for filepath, so we don't have to pass it every time in get_todos()

def get_todos(filepath=FILEPATH): # default value for filepath is 'todos.txt' so we don't have to pass it every time in get_todos()
    """Read a text file and return the list of to-do items."""

    with open(filepath, 'r') as file_local:
        open_todos = file_local.readlines()
    return open_todos

def write_todos(todos_arg, filepath=FILEPATH): # if another arugment with filepath, that should go first (todos_arg)
    """Write the to-do items list in the text file."""

    with open(filepath, 'w') as file:
            file.writelines(todos_arg)

