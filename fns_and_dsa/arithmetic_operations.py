from arithmetic_operations import perform_operation
def main:
    num1= float(input("Enter the first number: "))
    num2= float(input("Enter the second number: "))
    operation = input("Enter the operation(add, substract, multiply, divide): ").strip().lower()
    result = perform_operation(num1, num2, operation)
    print(f"Result:{result} ")
if_name_== "_main_":
    main()

