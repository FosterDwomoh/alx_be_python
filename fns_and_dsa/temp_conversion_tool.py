FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius (fahrenheit):
    CELSIUS_TO_FAHRENHEIT_FACTOR = (fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR
    return CELSIUS_TO_FAHRENHEIT_FACTOR
def convert_to_fahrenheit(celsius):
    FAHRENHEIT_TO_CELSIUS_FACTOR = celsius*CELSIUS_TO_FAAHRENHEIT_FACTOR+32
    return FAHRENHEIT_TO_CELSIUS_FACTOR
def main()
while True:
    try:
        temperature_str = input("Enter temperature (e.g.,32 F or 0 C): ").strip().upper()
        temperature_value = float(temperature_str[:-1].strip()
                temperature_unit = temperature_str[-1]
                if temperature_unit == 'F':
                converted_temperature = convert_to_celsius(temperature_value)
                print(f" {temperature_value} Fahrenheit is {converted_temperature:.2f} Celsius)
                elif temperature_unit == "C":
                converted_temperature = convert_to_fahrenheit(temperature_value)
                print(f "{temperature_value} celsius {converted_temperature: . 2f} Fahrenheit
                else:
                raise ValueError("Invalid temperature unit: please enter 'F' or 'C' ")
                break
                except ValueError:
                print("Invalid temperature. Please enter a numeric value followed by "F" or "C". ")
                except Exception as e:
                print(f" Error: {e}")
                if_name_=="_main_":
                main()
