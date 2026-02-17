"""
  A dictionary in Python is a mutable, unordered collection that stores data in key–value pairs, where each key is unique and is used to access its corresponding value.
"""
# Dictionary Example
capitals = {
    "AP" : "Amaravathi",
    "Kerala" : "Kochi",
    "TamilNadu" : "Chennai"
}
print(capitals)

student = {
    "name": "Ramesh",
    "age": 22,
    "branch": "ECE"
}

#Accessing the elements
print(student.get("name"))

#Eaxmple
data = {"a": 1, "b": 2, "c": 3}

print(data.keys())
print(data.values())
print(data.items())

#Update
data.update({"d": 4})
print(data)

# data.pop("a") removes the key or values

#data.popitem() Removes last inserted key–value pair.

# data.clear() Removes all items

# Creates a shallow copy.
# new_data = data.copy()

# Returns value if key exists, else inserts key.
data.setdefault("e", 5)
print(data)

#Keys
for k in data:
    print(k)

#Values
for v in data.values():
    print(v)

#Items
for k ,v in data.items():
    print(k ,v)

#Check key existence
print("a" in data)

#Inserting the sets and lists into the dictionary
#List as values
student = {
    "name": "Ramesh",
    "marks": [85, 90, 78],
    "skills": ["Python", "Angular"]
}

print(student["marks"])

#List as a keys will be possible
# data = {[1, 2]: "numbers"}  # Error

#Set as values
data = {
    "subjects": {"Maths", "Physics", "CS"},
    "years": {2022, 2023}
}

print(data["subjects"])

#Set as keys (NOT allowed)
#data = {{1, 2, 3}: "numbers"}  # Error

employees = [
    {"id" : 1, "name" : "Harsha", "role" : "QA"},
    {"id": 2, "name": "Anil", "role": "Developer"},
    {"id": 3, "name": "Ravi", "role": "Manager"}
]

print(employees[0])
print(employees[0]["name"])

for emp in employees:
    print(emp["name"], emp["role"])

for emp in employees:
    if emp["name"] == "Harsha":
        print(emp)
