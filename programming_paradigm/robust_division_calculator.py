# robust_division_calculator
def safe_divide(numerator, denominator):
    if denominator == 0:
        return "Error: Cannot divide by zero."
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num/denom
        print("Error: The result of the division is {result}")
        except ValueError:
            print("Error: Please enter numeric values only.")
            except ZeroDivisionError:
                print("Cannot divide by zero")
