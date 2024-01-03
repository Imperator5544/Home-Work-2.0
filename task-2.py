"""
Користувач вводить з клавіатури кількість метрів.
Залежно від вибору користувача програма переводить метри милі, дюйми або ярди.
"""
def meters_to_miles(meters):
    return meters * 0.000621371

def meters_to_inches(meters):
    return meters * 39.3701

def meters_to_yards(meters):
    return meters * 1.09361

# Getting user input
meters = float(input("Enter the number of meters: "))

# Selection of measurement units
print("Select units of measurement:")
print("1. Miles")
print("2. Inches")
print("3. Yards")

choice = input("Enter selection number: ")


# Conversion and display of the result
if choice == '1':
    result = meters_to_miles(meters)
    print(f"{meters} meters is equal to {result} miles")
elif choice == '2':
    result = meters_to_inches(meters)
    print(f"{meters} meters is equal to {result} inches")
elif choice == '3':
    result = meters_to_yards(meters)
    print(f"{meters} meters is equal to {result} yards")
else:
    print("Invalid selection. Please enter the correct number.")