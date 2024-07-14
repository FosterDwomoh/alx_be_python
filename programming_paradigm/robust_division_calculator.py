# robust_division_calculator
def safe_divide(numerator, denominator):
    if denominator == 0:
        return "Error:Division by Zero is not allowed."
    try:
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Please provide numeric input."
    result = num/denom
    return result
