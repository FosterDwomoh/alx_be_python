from arithmetic_operations import perform_operation
def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Division by zero is not allowed"
        else:
            return num1 / num2
        else:
            raise ValueError("Unsupported operation. Please use 'add','subtract', 'multiply', 'divide'.")
    num1= float(input("Enter the first number: "))
    num2= float(input("Enter the second number: "))
    operation = input("Enter the operation(add, subtract, multiply, divide): ").strip().lower()
    result = perform_operation(num1, num2, operation):
        print(f "Result:{result} ")
if_name_== "_main_":
    main()

