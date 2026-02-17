# Normal function
"""
A lambda function is a small, anonymous (nameless) function written in one line.
"""
from functools import reduce


def add(a,b):
    return a + b
print(add(2,4))

#In-terms of Lambda Expression
add = lambda a, b: a + b
print(add(1,2))

evenOdd = lambda a : "Even" if a % 2 == 0 else "Odd"
print(evenOdd(5))
print(evenOdd(10))

#Built-In Functions in Lambda Exp
#map() Applies function to each element.

nums = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, nums))
print(squares)

#filter()
numbers = [1,2,3,4,5,6,7,8,10,-1,-2,-10,-5]
even = list(filter(lambda x : x % 2 == 0, numbers))
print(even)

pos = list(filter(lambda x: x > 0, numbers))
print(pos)

#sorted with key
names = ["apple", "banana", "kiwi"]
print(sorted(names, key=lambda x: len(x)))

#reduce() - Aggregate - Combining many values to a one result
nums1 = [10,1,120,45,24]
h = reduce(lambda x, y: x + y, nums1)
print(h)

mul = reduce(lambda x ,y : x*y, nums1)
print(mul)

#marks = {'A':75, 'B': 90,'C': 55}

# Comprehensions provide a concise syntax to create new collections by iterating over an iterable with optional conditions.
#Comprehensions are a short and clean way to create collections (list, set, dictionary, generator) in one line
# Implementation: [expression for item in iterable if condition]

#List Example
squares = [x*x for x in range(1, 6)]
print(squares)

#Set Example
nums = [1, 2, 2, 3]
s = {x*x for x in nums}
print(s)

#Dictionary Example
employees = {
    "Harsha" : "Active",
    "Amit" : "Inactive",
    "Ravi" : "Active"
}
active_emp = {k:v for k, v in employees.items() if v == "Active"}
print(active_emp)