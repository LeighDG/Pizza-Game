from os import system, name

def clearConsole():
    # code from: https://www.geeksforgeeks.org/clear-screen-python/
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')