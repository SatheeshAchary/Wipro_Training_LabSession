# Car Class
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

car1 = Car("BMW", "X5", 5000000)
print(car1.brand, car1.model, car1.price)

# Student Class with get_grade()
class Student:
    def __init__(self, marks):
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        else:
            return "C"

s = Student(85)
print(s.get_grade())

# BankAccount Class
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.balance)

# Employee with init
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

e1 = Employee("Satheesh",12345,30000)
print(e1.name, e1.emp_id, e1.salary)

# Count Objects Created
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

obj1 = Counter()
obj2 = Counter()

print("Objects created:", Counter.count)

# Class Variable
class Company:
    company_name = "TechCorp"

    def __init__(self, employee_name):
        self.employee_name = employee_name

print(Company.company_name)

# Static Method (Email Validation)
class Validator:

    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email

print(Validator.validate_email("test@mail.com"))

# INHERITANCE
# Base → Derived
class Vehicle:
    def start(self):
        print("Vehicle started")

class Bike(Vehicle):
    def ride(self):
        print("Bike riding")

b = Bike()
b.start()
b.ride()

# Multilevel Inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

# Method Overriding with super()
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")

d = Dog()
d.sound()

# ENCAPSULATION
# Private Balance
class BankAccount:
    def __init__(self):
        self.__balance = 0   # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# Getter & Setter
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount

    def get_balance(self):
        return self.__balance

# Property Decorator (Prevent Negative Salary)
class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            print("Salary cannot be negative")
        else:
            self._salary = value

# POLYMORPHISM
# Shape Area

import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Method Overloading (Default Arguments)
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5))
print(calc.add(5, 10))
print(calc.add(5, 10, 15))

# Operator Overloading
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)
print(n1 + n2)

# COMPOSITION
# Engine inside Car
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

c = Car()
c.start()

# Team contains Player objects
class Player:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

team = Team()
p1 = Player("Ramesh")
team.add_player(p1)

