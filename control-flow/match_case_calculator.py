num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number:"))
operation= input("choose the operation (+, *, -, /): ")
result = 0
match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        result = num1 / num2
        if num2 == 0:
            print("error: division by zero not allowed." )
        else:
            result = num1 / num2
        case_:
            print(f"error: '{operation}' is not a valid operation.")
        if operation == '/' and num2 == 0:
            pass
        else:
            print(f"the result is {result}")
