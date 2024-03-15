from cowsay import tux, cow, dragon, turtle
from random import choice


def fun_console(text):
    functions = [tux, dragon, cow, turtle]
    random_function = choice(functions)
    random_function(text)


fun_console("Olá Python!")
