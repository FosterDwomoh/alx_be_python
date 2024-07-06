from arithmetic_operations import perform_operation
def main:
    num1= float(input("Enter the first number: "))
    num2= float(input("Enter the second number: "))
    operation= input("Enter the operation(add/substract/multiply/divide): ")
    result = perform_operation(num1, num2, operation)
    if isinstance(result,float):
        print(f"Result of {operation} operation:{result} ")
    else:
        print(result)
        if_name_== "_main_":
            main()
