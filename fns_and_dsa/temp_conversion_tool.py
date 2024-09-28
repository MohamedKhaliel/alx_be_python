FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temperature =float(input("Enter the temperature to convert: "))

def convert_to_celsius(fahrenheit):
    fahrenheit = (temperature - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(temperature ,"°F is ", fahrenheit, "°C")

def convert_to_fahrenheit(celsius):
    celsius = (temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(temperature ,"°C is ", celsius, "°F")

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if unit == 'F':
    convert_to_celsius(temperature)
elif unit == 'C':
    convert_to_fahrenheit(temperature)
else:
    print("Invalid temperature. Please enter a numeric value.")