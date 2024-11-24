def open_todos(filepath="todos.txt"):
    """ Read a text-file and return as a file."""
    with open(filepath, 'r') as file_open:
        todos_open = file_open.readlines()
        return todos_open

def write_todos(todos_arg, filepath="todos.txt"):
    """ Write a to-do item in this todos app."""
    with open(filepath, 'w') as file_write:
        file_write.writelines(todos_arg)

