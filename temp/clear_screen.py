import os
import subprocess


# both work for all platforms windows, linux and macOS
def clear_1():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def clear_2():
    subprocess.call('clear' if os.name == 'posix' else 'cls')


clear_1()
clear_2()
