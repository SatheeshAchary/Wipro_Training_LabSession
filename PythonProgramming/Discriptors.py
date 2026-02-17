#A descriptor is a class that controls access to another class’s attributes using special methods:

# __get__() → read the value

# __set__() → modify the value

# __delete__() → delete the value

class AgeDescriptor:
    def __get__(self, obj, objtype=None):
        return obj._age

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        obj._age = value

    def __delete__(self, obj):
        del obj._age

class Person:
    age = AgeDescriptor()

    def __init__(self, age):
        self.age = age

p = Person(25)

print(p.age)      # calls __get__()
p.age = 30        # calls __set__()
print(p.age)

del p.age         # calls __delete__()
