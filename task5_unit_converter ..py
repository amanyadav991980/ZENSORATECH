# Task 5: Unit Converter (Weight & Temperature)

def kg_to_pounds(kg):
    return round(kg * 2.2, 2)

def celsius_to_fahrenheit(c):
    return round((c * 9/5) + 32, 2)

print("--- Unit Converter ---")
print("1. Kilograms to Pounds")
print("2. Celsius to Fahrenheit")

choice = input("Choose an option (1 or 2): ")

if choice == '1':
    kg = float(input("Enter weight in kilograms: "))
    if kg < 0:
        print("Weight cannot be negative.")
    else:
        pounds = kg_to_pounds(kg)
        print(f"{kg}kg is equal to {pounds} lbs.")

elif choice == '2':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F.")

else:
    print("Invalid option. Please choose 1 or 2.")
