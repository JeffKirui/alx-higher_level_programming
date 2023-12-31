#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, div, sub, mul
    from sys import argv, exit

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operations = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": div
    }

    if argv[2] not in list(operations.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    # If the validations are OK, call the print function
    a = int(argv[1])
    b = int(argv[3])
    print("{} {} {} = {}".format(a, argv[2], b, operations[argv[2]](a, b)))
