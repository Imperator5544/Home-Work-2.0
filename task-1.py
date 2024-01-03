print("Enter any three numbers")
"""
Користувач вводить три цифри з клавіатури. 
Залежно від вибору користувача програма виводить на екран максимум із трьох, 
мінімум із трьох або середньоарифметичне трьох чисел.
"""
number_first = float(input("Enter first number: "))
number_second = float(input("Enter second number"))
number_third = float(input("Enter third number"))

operation = input("Select an operation: 'min','max','avg'")

if operation == "min":
    result = min(number_first, number_second, number_third)
    print(f"Minimum {result}")
elif operation == "max":
    result = max(number_first, number_second, number_third)
    print(f"Maximum {result}")
elif operation == "avg":
    result = (number_first + number_second + number_third) / 3
    print(f"Average {result}")
