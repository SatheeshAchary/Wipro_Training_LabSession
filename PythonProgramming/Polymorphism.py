# Polymorphism -- to act or take multiple arguments
# same method / function name will behave differently depending on the
# Object type
# input arguments
# class implementation

print(len("Satheesh"))
print(len([1,2,3,4,5]))
print(len((1,2,3,4,5,6)))


# Overriding
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

animals = [Dog(), Cat()]

for a in animals:
    a.sound()

# Method Over-loading
def add(a, b=0, c=0):
    return a + b + c


class Calculator:
    pass

calc = Calculator()

print(add(5))
print(add(5, 10))
print(add(5, 10, 15))
print()
# Polymorphism Operators
# ( + ) Operator
print(5 + 3)          # 8  (addition)
print("Py" + "thon")  # Python (concatenation)
print([1, 2] + [3])   # [1, 2, 3] (list merge)
print()
# ( * ) Operator
print(3 * 4)        # 12
print("Hi" * 3)     # HiHiHi
print([1] * 4)      # [1, 1, 1, 1]

print()
# ( == ) Operator
class Student:
    def __init__(self, marks):
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks

s1 = Student(80)
s2 = Student(80)

print(s1 == s2)


# Diamond Problem is solved by using MRO - Method Resolution Order
# Takes from left to right classes
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()

print()
# Using the super() to solve Diamond Problem
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        super().show()
        print("B")

class C(A):
    def show(self):
        super().show()
        print("C")

class D(B, C):
    def show(self):
        super().show()
        print("D")

d = D()
d.show()
