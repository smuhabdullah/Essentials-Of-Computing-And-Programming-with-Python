# Certainly! Object-oriented programming (OOP) in Python is based on four main 
# principles, often referred to as the "four pillars of OOP." These pillars are:

# Inheritance: This is the ability of a class to inherit properties and methods 
# from another class. It promotes code reusability and allows the creation of a 
# new class based on an existing class.
# 1. Inheritance

class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        # Call the constructor of the parent class using super()
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

    def display_info(self):
        # Override the display_info method of the parent class
        return f"{super().display_info()} - Electric, Battery: {self.battery_capacity} kWh"

# Creating an instance of the ElectricCar class
my_electric_car = ElectricCar("Tesla", "Model S", 100)

# Accessing the inherited and overridden methods
print("2. Inheritance:", my_electric_car.display_info())
print()

# Encapsulation: This involves bundling data (attributes) and the methods 
# (functions) that operate on the data into a single unit known as a class. 
# Access to the data is restricted to methods of the class.
# 2. Encapsulation

class Car:
    def __init__(self, make, model):
        self.__make = make  # Private attribute
        self.__model = model  # Private attribute

    def display_info(self):
        return f"{self.__make} {self.__model}"

# Creating an instance of the Car class
my_car = Car("Toyota", "Camry")

# Accessing the private attributes through a public method
print("1. Encapsulation:", my_car.display_info())
print()

# Polymorphism: This allows objects of different classes to be treated as objects 
# of a common base class. It enables a single interface to represent different types 
# of objects.

# 3. Polymorphism

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# Creating instances of different shapes
circle = Circle(5)
square = Square(4)

# Using a common interface to calculate area
print("3. Polymorphism:")
print("   Circle Area:", circle.area())
print("   Square Area:", square.area())
print()


# Abstraction: This involves simplifying complex systems by modeling classes based on 
# the essential properties and behaviors they share. It hides the complex implementation
# details and shows only the necessary features of an object.

# 4. Abstraction

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Creating instances of different animals
dog = Dog()
cat = Cat()

# Using the abstracted interface to make sounds
print("4. Abstraction:")
print("   Dog Sound:", dog.make_sound())
print("   Cat Sound:", cat.make_sound())


# ------------------------------------------------------------------------------------------------------------------------
# The four pillars of OOP are the foundation of object-oriented programming.
# Inheritance allows a class to inherit properties and methods from another class.
# Encapsulation bundles data and methods into a single unit known as a class.
# Polymorphism allows objects of different classes to be treated as objects of a common base class.
# Abstraction simplifies complex systems by modeling classes based on the essential properties and behaviors they share.

# ------------------------------------------------------------------------------------------------------------------------

# Solve the following problems using the four pillars of OOP.

# 1. Create a class named Person with the following properties/methods:
# Properties: first_name, last_name, age
# Methods: display_info() - prints the values of all three properties

# Create a class named Student that inherits from the Person class. The Student class should have the following properties/methods:
# Properties: student_id, gpa
# Methods: display_info() - prints the values of all five properties

# Create a class named Teacher that inherits from the Person class. The Teacher class should have the following properties/methods:
# Properties: teacher_id, salary
# Methods: display_info() - prints the values of all five properties

# Create an instance of the Student class and call its display_info() method.
# Create an instance of the Teacher class and call its display_info() method.

# The End of the first problem
# ------------------------------------------------------------------------------------------------------------------------

# 2. Create a class named Shape with the following properties/methods:
# Properties: color
# Methods: area() - returns 0.0

# Create a class named Circle that inherits from the Shape class. The Circle class should have the following properties/methods:
# Properties: radius
# Methods: area() - returns the area of the circle

# Create a class named Square that inherits from the Shape class. The Square class should have the following properties/methods:
# Properties: side
# Methods: area() - returns the area of the square

# Create an instance of the Circle class and call its area() method.
# Create an instance of the Square class and call its area() method.

# The End of the second problem
# ------------------------------------------------------------------------------------------------------------------------

# 3. Create a class named Animal with the following properties/methods:
# Properties: name
# Methods: make_sound() - returns an empty string

# Create a class named Dog that inherits from the Animal class. The Dog class should have the following properties/methods:
# Properties: breed
# Methods: make_sound() - returns "Woof!"

# Create a class named Cat that inherits from the Animal class. The Cat class should have the following properties/methods:
# Properties: breed
# Methods: make_sound() - returns "Meow!"

# Create an instance of the Dog class and call its make_sound() method.
# Create an instance of the Cat class and call its make_sound() method.

# The End of the third problem
# ------------------------------------------------------------------------------------------------------------------------

# 4. Create a class named Vehicle with the following properties/methods:
# Properties: make, model
# Methods: display_info() - prints the values of all two properties

# Create a class named Car that inherits from the Vehicle class. The Car class should have the following properties/methods:
# Properties: make, model, fuel_capacity
# Methods: display_info() - prints the values of all three properties

# The End of the fourth problem
# ------------------------------------------------------------------------------------------------------------------------

