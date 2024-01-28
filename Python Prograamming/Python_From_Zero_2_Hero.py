# Hello, World! - A basic Python program
print("Hello, World!")

# Variables and Data Types
name = "Muhammad Abdullah"
age = 30
height = 175.5
is_student = True

# Basic Input/Output
user_input = input("Enter your name: ")
print("Hello, " + user_input)

# Conditional Statements
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Loops
for i in range(1, 5):
    print("Iteration", i)

# Lists and Iteration
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)

# Functions
def greet(name):
    print("Hello, " + name)

greet("Alice")

# Dictionaries
student = {
    "name": "Muhammad Abdullah",
    "age": 23,
    "major": "Computer Science"
}
print(student["name"])

# Classes and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is", self.name)

person1 = Person("Muhammad Abdullah", 23)
person1.say_hello()

# Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)

# File Handling
with open("sample.txt", "w") as file:
    file.write("This is a sample file.")

with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:", content)

# Libraries and Modules
import math
print("Square root of 16:", math.sqrt(16))

# Advanced Concepts (Optional)
# - List comprehensions
# - Generators
# - Decorators
# - Context Managers
# - Threading/Multiprocessing

# You can continue to explore more Python concepts and libraries based on your interests and needs.



# List Comprehensions
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)  # [1, 4, 9, 16, 25]

# Generators
def generate_numbers(n):
    for i in range(n):
        yield i

gen = generate_numbers(3)
print(next(gen))  # 0
print(next(gen))  # 1

# Decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Context Managers
with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:", content)

# Threading and Multiprocessing (Concurrency)
import threading
import multiprocessing

def print_numbers():
    for i in range(1, 6):
        print("Thread 1:", i)

def print_letters():
    for letter in "abcde":
        print("Thread 2:", letter)

# Create and start two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)
thread1.start()
thread2.start()

# Multiprocessing example
def square_number(number):
    print(f"Square of {number}: {number**2}")

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    processes = []

    for number in numbers:
        process = multiprocessing.Process(target=square_number, args=(number,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

# This is just a glimpse of advanced concepts. Python offers a wide range of libraries and modules for various tasks.
# You can explore topics like web development (Django, Flask), data analysis (Pandas, NumPy), machine learning (Scikit-Learn),
# and more based on your interests and projects.

# Keep practicing and building projects to become proficient in Python!

