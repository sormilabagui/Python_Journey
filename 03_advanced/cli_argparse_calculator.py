# cli_argparse_calculator.py
# Demonstrating a CLI tool using argparse

import argparse

# Create parser
parser = argparse.ArgumentParser(description="Simple CLI Calculator")

# Add arguments
parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")
parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help="Operation to perform")

# Parse arguments
args = parser.parse_args()

# Perform operation
if args.operation == "add":
    result = args.num1 + args.num2

elif args.operation == "sub":
    result = args.num1 - args.num2

elif args.operation == "mul":
    result = args.num1 * args.num2

elif args.operation == "div":
    if args.num2 == 0:
        print("Cannot divide by zero")
        exit()
    result = args.num1 / args.num2

print("Result:", result)