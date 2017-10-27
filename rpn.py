#!/usr/bin/env python3
import readline  # noqa: F401
import operator
from termcolor import colored


ops = {
    '+': operator.add,
    '-': operator.sub,
    '^': operator.pow
}


def calculate(arg):
    stack = list()
    for token in arg.split():
        try:
            stack.append(int(token))
        except ValueError:
            arg2 = stack.pop()
            arg1 = stack.pop()
            to_print = str(arg1) + " " + colored(token, "magenta") + " " + str(arg2)
            function = ops[token]
            result = function(arg1, arg2)
            if result < 0:
                to_print += " = " + colored(str(result), "red")
            else:
                to_print += " = " + colored(str(result), "cyan")
            print(to_print)
            stack.append(result)
    return stack.pop()


def reduce_coverage():
    i = 100
    while i > 0:
        i -= 1
    pass


def main():
    total_input = ""
    print("Type = to calculate")
    while True:
        user_input = input("rpn calc> ")
        if user_input == "=":
            break
        else:
            total_input += str(user_input) + " "

    print("Calculating result...")
    calculate(total_input)



if __name__ == '__main__':
    main()
