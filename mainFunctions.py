

def todo_list(filename="Todos.txt"):
    """A function that reads and makes a list of items in the file"""
    with open(filename, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filename="Todos.txt"):
    """A function that writes and stores it in a file"""
    with open(filename, 'w') as file_writen:
        file_writen.writelines(todos_arg)
