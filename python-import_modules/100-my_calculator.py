import sys
from calculator_1 import *
if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])