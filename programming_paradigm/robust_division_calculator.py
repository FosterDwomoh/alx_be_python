# robust_division_calculator
def safe_divide(numerator, denominator):
    if denominator == 0:
        return "Error: Cannot divide by zero."
    try:
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    result = num/denom
    return result
