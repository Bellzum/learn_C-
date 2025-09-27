try:
    in1 = float(input("Enter first number: "))
    in2 = float(input("Enter second number: "))
except ValueError:
    print("Input error")
    raise SystemExit(1)

operation = input("Enter the operation '+', '-', '*', '/' ");


if operation == '+':
    answer = in1 + in2
elif operation == '-':
    answer = in1 - in2
elif operation == '*':
    answer = in1 * in2
elif operation == '/':
    if in2 == 0:
        print("Cannot divide by zero")
        answer = None
    else:
        answer = in1 / in2
else:
    print("Unknown operation")
    answer = None

if answer != None:
    print(f"{in1} {operation} {in2} = {answer}")