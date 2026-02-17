#Exceptions are the Unknown event occurs due to the faulsely input given or wrong logic written by the developer
# To Handle it we have to use "try" and "except" blocks
# It prevents program crash
from importlib import invalidate_caches
from logging import exception

#try-except
try:
    a = int(input("Enter the Number:"))
    b = int(input("Enter the number:"))
    print(a/b)
except ZeroDivisionError:
    print("Number cannot be divided by 0")

########################
try:
    a = 10/2
except Exception as e:
    print(e)

else:
    print("Divison Successfull")

finally:
    print("Running Stopped!")

####################
age = int(input("Enter your Age:"))
try:
   if age >= 18:
      print("Good..You are allowed to vote")
except:
    raise AttributeError("Age should be Greater than 18")

######################
try:
    with open("C://Users//WINDOW 11//PycharmProjects//PythonAdvancedProgramming//Dataframes//employees.json", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found. Please check the file path.")

#########################
try:
    a = int(input("Enter the number"))
    b = int(input("Enter the second number"))
    print(a/b)
except invalidate_caches() as e:
    print(e)

###############################

