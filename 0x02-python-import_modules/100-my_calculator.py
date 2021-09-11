#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == '__main':
    if argv != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
	exit(1)
 
    opr = argv[2]
    if argv[2] != '+' and argv[2] != '-' and argv[2] != '*' and argv[2] != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    f = {"+": add, "-": sub, "*": mul, "/": div}
    print("{:d} {:s} {:d} = {:d}".format(a, op, b, f[opr](a, b)))
