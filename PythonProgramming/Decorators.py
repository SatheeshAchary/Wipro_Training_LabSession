# Decorators -- Which is used to decorate or modify the function which is already exits using the another function without changing the main function
# Wrapper function around the functions
# Example

def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def hello():
    print("Hello")

hello()

#Example
def func1(func):
    def innerfunc():
        print("This is inner Function")
        func()
        print("Execution of the main func")
    return innerfunc

@my_decorator
def mainfunc():
    print("Hey...buddy!")

mainfunc()