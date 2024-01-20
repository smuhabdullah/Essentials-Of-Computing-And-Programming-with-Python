# Question1 - Write a Python program to do arithmetical operations addition and division.

# Arithmetical operations
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Addition
addition_result = num1 + num2
print(f"Addition: {num1} + {num2} = {addition_result}")

# Division
division_result = num1 / num2
print(f"Division: {num1} / {num2} = {division_result}")

# Power
power_result = num1 ** num2
print(f"Power: {num1} ^ {num2} = {power_result}")

# Floor Division
floor_division_result = num1 // num2
print(f"Floor Division: {num1} // {num2} = {floor_division_result}")

# End of Question1

# This is example if we want to use the multiple operations
# Multiple operations
result = ((num1 + num2) * num1) / (num2 - num1)
print(f"Multiple Operations: (({num1} + {num2}) * {num1}) / ({num2} - {num1}) = {result}")

# ---------------------------------------------------------------

# Question2 - Write a Python program to find the area of a triangle.

# Area of a triangle
base = 5
height = 8
triangle_area = 0.5 * base * height
print(f"Area of Triangle with base {base} and height {height}: {triangle_area}")

# End of Question2
# ---------------------------------------------------------------

# Question3 - Write a Python program to convert Celsius to Fahrenheit.

# Celsius to Fahrenheit conversion
celsius_temperature = 25
fahrenheit_temperature = (celsius_temperature * 9/5) + 32
print(f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_temperature:.2f} degrees Fahrenheit")

# End of Question3
# ---------------------------------------------------------------

# Question4 - Write a Python program that reads two integers representing a month and day and prints the season for that month and day.
# Data types

# Integers
number = 10
float_number = 10.5
string = "Hello World"
boolean = True
lst = [1, 2, 3, 4, 5]
tup = (1, 2, 3, 4, 5)
set = {1, 2, 3, 4, 5}
dict = {"name": "Muhammad Abdullah", "age": 36}

# Print data types
print(f"The data type of {number} is {type(number)}")
print(f"The data type of {float_number} is {type(float_number)}")
print(f"The data type of {string} is {type(string)}")
print(f"The data type of {boolean} is {type(boolean)}")
print(f"The data type of {lst} is {type(lst)}")
print(f"The data type of {tup} is {type(tup)}")
print(f"The data type of {set} is {type(set)}")
print(f"The data type of {dict} is {type(dict)}")

# End of Question4
# ---------------------------------------------------------------


## For Practice do following questions
#### 1 - Write a Python program to calculate the area and circumference of a circle. Use a given radius.
#### 2 - Write a Python program to convert a distance in kilometers to miles. Take the distance in kilometers as user input.
#### 3 - Write a python program that check whether the number is even or odd.