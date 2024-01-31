# ------------------------------------------------------------------------------------------------------------------------
# Lets get started
# ------------------------------------------------------------------------------------------------------------------------

#Certainly! Object-oriented programming (OOP) is a programming paradigm based on the concept of objects, which can contain data (attributes) and code (methods). 
#In Python, OOP is implemented through classes and objects. Let's start by explaining attributes and methods in OOP, and then we'll delve into the four pillars of OOP.

# ------------------------------------------------------------------------------------------------------------------------
#Attributes and Methods in OOP:
# ------------------------------------------------------------------------------------------------------------------------

#Attributes:
#Attributes are characteristics or properties that describe an object. They are like variables associated with an object and store data specific to that object. 
#Attributes represent the state of the object. In Python, attributes are defined within a class and can have different data types.
# ------------------------------------------------------------------------------------------------------------------------
class Car:
    def __init__(self, make, model, year):
        self.make = make       # Attribute: Make of the car
        self.model = model     # Attribute: Model of the car
        self.year = year       # Attribute: Year of manufacture

my_car = Car("Toyota", "Camry", 2022)
print(my_car.make)  # Accessing the 'make' attribute
print(my_car.year)  # Accessing the 'year' attribute

# ------------------------------------------------------------------------------------------------------------------------
#Methods:
#Methods are functions defined within a class that can perform actions on the object's data (attributes). Methods define the behavior of the object. 
#In Python, methods are also defined within a class and can be used to manipulate the object's attributes.
# ------------------------------------------------------------------------------------------------------------------------

class Circle:
    def __init__(self, radius):
        self.radius = radius  # Attribute: Radius of the circle

    def calculate_area(self):
        return 3.14 * self.radius * self.radius  # Method: Calculate the area of the circle

my_circle = Circle(5)
area = my_circle.calculate_area()
print(f"Area of the circle: {area}")

# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------

# The Four Pillars of OOP:
# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------

# Now, let's explore the four pillars of OOP, which are key principles that guide object-oriented design:

# ------------------------------------------------------------------------------------------------------------------------
# Encapsulation:

# Encapsulation is the concept of bundling data (attributes) and methods (functions) that operate on that data into a single unit called a class.
# It allows us to hide the internal details of how an object works and provides an interface (public methods) for interacting with the object.
# Encapsulation helps in data protection and reduces complexity.

# ------------------------------------------------------------------------------------------------------------------------
# Inheritance:

# Inheritance is a mechanism that allows a new class (subclass or derived class) to inherit properties and behaviors from an existing class (base class or superclass).
# It promotes code reuse by creating a hierarchy of classes where a subclass inherits attributes and methods from its superclass.
# It facilitates the creation of specialized classes based on more general ones.

# ------------------------------------------------------------------------------------------------------------------------
# Polymorphism:

# Polymorphism means "many forms" and refers to the ability of different objects to respond to the same method or function in a way that is appropriate for their own specific type.
# It allows objects of different classes to be treated as objects of a common superclass through method overriding and method overloading.

# ------------------------------------------------------------------------------------------------------------------------
# Abstraction:

# Abstraction is the process of simplifying complex reality by modeling classes based on the essential properties and behaviors of objects.
# It involves defining a class with a clear interface while hiding the unnecessary implementation details.
# Abstraction allows us to focus on what an object does, rather than how it does it.
# These four pillars collectively form the foundation of object-oriented programming and enable the creation of well-structured and maintainable code. 
# Each pillar plays a crucial role in designing and organizing classes and objects in Python and other object-oriented languages.

# ------------------------------------------------------------------------------------------------------------------------
# Certainly! Let's dive into each of the four pillars of Object-Oriented Programming (OOP) in Python, explaining them one by one in detail.

# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------

# 1. Encapsulation:
# Definition:
# Encapsulation is one of the fundamental concepts in OOP. It refers to the bundling of data (attributes) and methods (functions) that operate on that data into a single 
# unit called a class. The key idea is to hide the internal details of how an object works and provide a well-defined interface for interacting with the object.

# ------------------------------------------------------------------------------------------------------------------------
# Explanation:

# Encapsulation helps in data protection and reduces complexity by exposing only the necessary functionality to the outside world, keeping the internal workings hidden.
# In Python, encapsulation is implemented using access control mechanisms, primarily public, protected, and private access modifiers.
# Access Modifiers in Python:
# ------------------------------------------------------------------------------------------------------------------------

# Public: Attributes and methods declared without any access modifier are considered public. They can be accessed from anywhere.
class MyClass:
    def __init__(self):
        self.public_attribute = 10  # Public attribute

    def public_method(self):
        return "This is a public method."

obj = MyClass()
print(obj.public_attribute)  # Accessing public attribute
print(obj.public_method())    # Accessing public method

# Protected: Attributes and methods with a single underscore prefix (e.g., _protected_attribute) are considered protected. They should not be accessed from outside the class, 
# but Python does not enforce strict protection.

class MyClass:
    def __init__(self):
        self._protected_attribute = 20  # Protected attribute

    def _protected_method(self):
        return "This is a protected method."

obj = MyClass()
print(obj._protected_attribute)  # Accessing protected attribute (not recommended)
print(obj._protected_method())   # Accessing protected method (not recommended)

# Private: Attributes and methods with a double underscore prefix (e.g., __private_attribute) are considered private. They are strongly discouraged from being accessed
# directly from outside the class.

class MyClass:
    def __init__(self):
        self.__private_attribute = 30  # Private attribute

    def __private_method(self):
        return "This is a private method."

obj = MyClass()
# Accessing private attribute/method directly results in an AttributeError.
# print(obj.__private_attribute)
# print(obj.__private_method())

# ------------------------------------------------------------------------------------------------------------------------
# Benefits of Encapsulation:

# Data protection: Encapsulation prevents unauthorized access and modification of object attributes, ensuring data integrity.
# Modularity: It allows for modular and organized code by grouping related data and methods into classes.
# Code flexibility: Encapsulation enables changes to the internal implementation of a class without affecting code that uses the class.
# Code readability: By providing a clear interface, encapsulation makes code more readable and understandable.

# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------

# 2. Inheritance:
# Definition:
# Inheritance is a mechanism in OOP that allows a new class (subclass or derived class) to inherit properties and behaviors (attributes and methods) from an existing class (base class or superclass). It promotes code reuse and the creation of specialized classes based on more general ones.

# Explanation:

# Inheritance creates a hierarchical relationship between classes, where the subclass inherits the attributes and methods of the superclass.
# Python supports single inheritance (a subclass can inherit from one superclass) and multiple inheritance (a subclass can inherit from multiple superclasses).
# The super() function is used to access and call superclass methods from within a subclass.
# ------------------------------------------------------------------------------------------------------------------------
# Example of Inheritance:
# ------------------------------------------------------------------------------------------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # Abstract method, to be implemented by subclasses

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!

# ------------------------------------------------------------------------------------------------------------------------
# Benefits of Inheritance:

# Code reuse: Inheritance allows you to reuse attributes and methods from existing classes, reducing redundancy.
# Hierarchy: It helps organize classes into a hierarchy, with specialized classes inheriting from more general ones.
# Extensibility: You can extend the functionality of existing classes by adding new attributes and methods in subclasses.
# Polymorphism: Inheritance enables polymorphism, allowing objects of different classes to be treated as objects of a common superclass.
# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------

# 3. Polymorphism:
# Definition:
# Polymorphism means "many forms" and is a key concept in OOP. It refers to the ability of different objects to respond to the same method or function in a way that 
# is appropriate for their specific type. Polymorphism allows objects of different classes to be treated as objects of a common superclass.

# Explanation:

# Polymorphism is achieved through method overriding and method overloading.
# Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass.
# Method overloading involves defining multiple methods with the same name but different parameter lists (Python supports only a limited form of method overloading).

# ------------------------------------------------------------------------------------------------------------------------
# Example of Polymorphism (Method Overriding):
# ------------------------------------------------------------------------------------------------------------------------
class Bird:
    def speak(self):
        pass

class Parrot(Bird):
    def speak(self):
        return "Parrot says Hello!"

class Crow(Bird):
    def speak(self):
        return "Crow says Caw!"

bird1 = Parrot()
bird2 = Crow()

def describe(bird):
    return bird.speak()

print(describe(bird1))  # Output: Parrot says Hello!
print(describe(bird2))  # Output: Crow says Caw!

# ------------------------------------------------------------------------------------------------------------------------
# Benefits of Polymorphism:

# Flexibility: Polymorphism allows for flexible and dynamic code, where objects can be treated generically based on their common superclass.
# Extensibility: New classes can be added without affecting existing code that relies on polymorphism.
# Code readability: Polymorphism enhances code readability by promoting a common interface for objects of different classes.

# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------

# 4. Abstraction:
# Definition:
# Abstraction is the process of simplifying complex reality by modeling classes based on the essential properties and behaviors of objects. It involves defining a class with a clear interface while hiding the unnecessary implementation details.

# Explanation:

# Abstraction focuses on what an object does rather than how it does it.
# It allows developers to create classes with well-defined methods and attributes that abstract away the inner complexities.
# Abstract classes and methods serve as blueprints for more concrete subclasses to implement.
# ------------------------------------------------------------------------------------------------------------------------
# Example of Abstraction:
# ------------------------------------------------------------------------------------------------------------------------
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
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

circle = Circle(5)
square = Square(4)

print(circle.area())  # Output: 78.5
print(square.area())  # Output: 16

# ------------------------------------------------------------------------------------------------------------------------
# Benefits of Abstraction:

# Simplification: Abstraction simplifies complex systems by providing clear and high-level interfaces.
# Reusability: Abstract classes and methods can be reused in various subclasses.
# Focus on essentials: Abstraction allows developers to focus on the essential aspects of an object's behavior.
# These four pillars of OOP collectively form the foundation for designing and organizing classes and objects in Python, leading to well-structured and maintainable code.
# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------

# The four pillars of OOP are the foundation of object-oriented programming.
# Inheritance allows a class to inherit properties and methods from another class.
# Encapsulation bundles data and methods into a single unit known as a class.
# Polymorphism allows objects of different classes to be treated as objects of a common base class.
# Abstraction simplifies complex systems by modeling classes based on the essential properties and behaviors they share.

# ------------------------------------------------------------------------------------------------------------------------
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
# ------------------------------------------------------------------------------------------------------------------------

# Instructor: Muhammad Abdullah
# Portfolio: smuhabdullah.me
# ------------------------------------------------------------------------------------------------------------------------
