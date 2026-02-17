#  Class - class is like a blueprint of an object
#  - Object is a real-world entity
from tkinter.font import names

from PythonProgramming.Dictionary import student

class Student:
    # Creating the properties of the class
    studentName = input("Enter the Student Name:")
    studentRoll = int(input("Enter the student roll-number:"))
    studentCourse = input("Enter the course of the student:")

    # Creating the behaviour of the student class
    def display(self):
        print("My name is:",self.studentName)
        print("My Roll-Number is:",self.studentRoll)
        print("My course is:",self.studentCourse)

# Calling the class
a = Student()
a.display()

# Example 2:
class Employee:
    empId = input("Enter the employee ID:")
    empName = input("Enter the employee Name:")
    empDept = input("Enter the employee Department:")

    def displayDetails(self):
        print(self.empId)
        print(self.empName)
        print(self.empDept)

a = Employee()
a.displayDetails()
b = Employee()
b.displayDetails()

## Constructors -- Default Constructor
class Student1:
    def __init__(self):
        print("This the constructor call.....")

a = Student1()

# Parametrized Constructor
class Student2:
    def __init__(self,name,roll,course):
        self.name = name
        self.roll = roll
        self.course = course

    def display(self):
        print(self.name)
        print(self.roll)
        print(self.course)

d = Student2("Satheesh",1234,"python")
d.display()
e = Student2("Vijay",5678,"PythonDSA")
e.display()

## Constructor Over-loading is supported by "*args" keyword
## We can do with any number of parameters to the constructor using *args

class Numbers:
    def __init__(self, *args):
        self.values = args

n = Numbers(10,20,30,40,50)
print(n.values)

m = Numbers(2,3,4)
print(m.values)

p = Numbers(2)
print(p.values)

## Destructor Implementation
## it automatically clean up the space of the objects which are no longer used
# Destructors - when we want to destroy the object
# post conditions - cloisng of the browser , db coonectinon closing , reasing of certian resources
# clean up operations
# for  proper memory usage destcrutors should  be used
#  when db connection has to be closed -
# free the memory (garbage collection) which is automatically called
# Destructor runs when program ends or object is garbage-collected.


class Desct:
    def __init__(self):
        print("Objected is been Created")

    def __del__(self):
        print("Closing the DB connection")

h = Desct()
print("End of the program")
del h







