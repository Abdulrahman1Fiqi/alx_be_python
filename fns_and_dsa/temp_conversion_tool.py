CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9


def convert_to_celsius(fahrenheit):
    result = (fahrenheit -32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return result

def convert_to_fahrenheit(celsius):
    result = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return result

def main():
    temperature = input("Enter the temperature to convert: ")
    if temperature.isdigit() :
        temperature=float(temperature)
        temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
        if temperature_type.upper() == 'F':
            print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
        elif temperature_type.upper() == 'C':
            print(f"{temperature}°F is {convert_to_fahrenheit(temperature)}°C")
        else:
            print("error,try again")
    else:
        print("Invalid temperature. Please enter a numeric value.")
if __name__=="__main__":
    main()