# Function is block of code that is used to perform specific task or Operation
# to define the function we use "def" keyword and the "func name"
#Example

def printName():
    print("My name is Satheesh")

#Calling the function
printName()

#USing the Parameters
def add(a,b):
    c = a + b
    print(c)

add(10,20)

#function with single Parameter
#Using the return Statement
def printName(s):
    return f"Hello, {s}"
print(printName("Satheesh"))

def square(num):
    return num * num

print("Square of the number is:",square(5))

def func_pass():
    pass
print(func_pass())

#Using the Multiple return values with multiple variables
def cal(a,b):
    return a+b, a-b, a*b
add, sub, mul = cal(10,5)
print(add)
print(sub)
print(mul)

#To find the even numbers
def findEven(num):
    for i in range(0,num+1):
        if i % 2 == 0 :
            print(i)

findEven(10)

def even(n):
    if n % 2 == 0:
        print(n,"is even")
    else:
        print(n,"is odd!")
even(5)
even(10)