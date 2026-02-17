# Single Inheritance:

class Parent:
    def __init__(self):
        print("I am the Parent class")

class child(Parent):
    def __init__(self):
        super().__init__()
        print("I am the child class")

a = child()

##################################
# Single Inheritance
class Bird:
    def __init__(self,name,color):
        self.name = name
        self.color = color

class Eagle(Bird):
    def flyHigh(self):
        print(f"{self.name} eagle with {self.color} color is flying high......")

m = Eagle("Sarpant","Brown")
m.flyHigh()

## Example
class SavingsAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Updated Balance:", self.balance)

class AddInterest(SavingsAccount):
    def calculate_interest(self, rate, time):
        interest = (self.balance * rate * time) / 100
        print("Interest:", interest)
        print("Total Balance:", self.balance + interest)

acc = AddInterest("Satheesh", 123456, 10000)
acc.deposit(2000)                 # deposit money
acc.calculate_interest(4, 1)       # 4% interest for 1 year

# Multi-Level Inheritance
class A:
    def __init__(self):
        print("This is from class 'A'")

class B(A):
    def __init__(self):
        super().__init__()
        print("This is from class 'B'")

class C(B):
    def __init__(self):
        super().__init__()
        print("This is from class 'C'")

f = C()
print(f)

# Hierarchy Inheritance
class Company:
    def __init__(self,empName,empId):
        self.empName = empName
        self.empId = empId

class Developer(Company):
    def develop(self):
        print(f"Developer {self.empName} with {self.empId} logged Successfully..")

class Tester(Company):
    def test(self):
        print(f"Tester {self.empName} with {self.empId} logged Successfully...")

D = Developer("Satheesh","RS21345")
D.develop()
T = Tester("Vijay","RS98764")
T.test()

print()
## Multiple Inheritance
class Daddy:
    def ManagingSkills(self):
        print("Managing skills from the Daddy should be acquired")

class Mother:
    def CookingSkills(self):
        print("Cooking skills should be acquired from mother")

class Son(Daddy,Mother):
    def bothSkills(self):
        self.ManagingSkills()
        self.CookingSkills()

s = Son()
print(s.bothSkills())




