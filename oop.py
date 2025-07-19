# Task: Create a Class to Represent a Student

class Student:
    def __init__(self, name, age, grade):
        self.name = name        
        self.age = age          
        self.grade = grade  


student1 = Student("Asmit", 20, "A")


print("Name:", student1.name)
print("Age:", student1.age)
print("Grade:", student1.grade)


##
# Task: Difference Between Class Variable and Instance Variable

class Student:
    # Class variable 
    school_name = "Green Valley School"

    def __init__(self, name, grade):
        # Instance variables 
        self.name = name
        self.grade = grade


student1 = Student("Asmit", "A")
student2 = Student("Bina", "B")

# Accessing instance variables
print("Student 1 Name:", student1.name)
print("Student 2 Name:", student2.name)

# Accessing class variable
print("Student 1 School:", student1.school_name)
print("Student 2 School:", student2.school_name)

# Changing the class variable using the class name
Student.school_name = "Sunrise Academy"

# After change
print("Updated Student 1 School:", student1.school_name)
print("Updated Student 2 School:", student2.school_name)


##
# Task: Implement a Method in a Class

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    
    def show_profile(self):
        print("Student Profile:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)


student1 = Student("Asmit", 20, "A")


student1.show_profile()


##]
# Task: Use Private Variables in a Class

class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount.")

    def check_balance(self):
        print(f"Current balance: {self.__balance}")


account = BankAccount(1000)


account.deposit(500)


account.check_balance()


##
# Task: Use Getters and Setters

class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # private variable

    
    def get_balance(self):
        return self.__balance

    
    def set_balance(self, value):
        if value >= 0:
            self.__balance = value
            print("Balance updated.")
        else:
            print("Invalid balance. Must be non-negative.")

account = BankAccount(1000)

print("Current Balance:", account.get_balance())

account.set_balance(1500)


print("Updated Balance:", account.get_balance())


account.set_balance(-500)


##
# Task: Method Overriding Example


class Animal:
    def speak(self):
        print("The animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("The dog says: Woof!")


class Cat(Animal):
    def speak(self):
        print("The cat says: Meow!")


animal = Animal()
dog = Dog()
cat = Cat()


animal.speak()
dog.speak()
cat.speak()


##
# Task: Use Polymorphism with a Common Interface

class Animal:
    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("The dog says: Woof!")

class Cat(Animal):
    def speak(self):
        print("The cat says: Meow!")

class Cow(Animal):
    def speak(self):
        print("The cow says: Moo!")


animals = [Dog(), Cat(), Cow()]


for animal in animals:
    animal.speak()


##
# Task: Create a Base and Derived Class


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Derived class
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  
        self.doors = doors


my_car = Car("Toyota", "Corolla", 4)

print("Brand:", my_car.brand)
print("Model:", my_car.model)
print("Number of doors:", my_car.doors)

##
# Task: Multiple Inheritance

class Father:
    def skills(self):
        print("Father's skills: Gardening, Carpentry")

class Mother:
    def skills(self):
        print("Mother's skills: Cooking, Painting")

class Child(Father, Mother):
    def skills(self):
        print("Child inherits skills from both parents:")
        Father.skills(self)  
        Mother.skills(self)  


child = Child()
child.skills()


##
# Task: Use Abstract Base Class

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


rect = Rectangle(5, 3)
circle = Circle(4)


print("Rectangle area:", rect.area())
print("Circle area:", circle.area())
