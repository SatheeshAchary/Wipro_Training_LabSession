# JSON - JavaScript Object Notation
#JSON is a text-based format used to represent structured data using key–value pairs and arrays.
"""
JSON stands for JavaScript Object Notation.
It is a lightweight data-interchange format used to store and exchange data between systems (client ↔ server).
"""
#Opening the file and Reading the Data
import json

with open("C://Users//WINDOW 11//PycharmProjects//PythonAdvancedProgramming//Dataframes//employees.json", 'r') as file:
    data = json.load(file)

print(data)
print(data["name"])

with open("C://Users//WINDOW 11//PycharmProjects//PythonAdvancedProgramming//Dataframes//nestedjson.json", 'r') as file:
    data = json.load(file)

print(data)
print(data["user"]["profile"]["email"])

#Writing the data into the file
data = {
    "name" : "Adarsh",
    "role" : "Manager",
    "Exp" : 3,
    "email" : "adarshroyals@gmail.com"
}

with open("C://Users//WINDOW 11//PycharmProjects//PythonAdvancedProgramming//Dataframes//writingfile.json", 'w') as file:
     json.dump(data,file)

"""
To update a JSON file, you cannot directly update it like a database.
You must follow this 3-step process:

# Read → Modify → Write back
"""
#Reading the file
with open("C://Users//WINDOW 11//PycharmProjects//PythonAdvancedProgramming//Dataframes//writingfile.json", 'r') as file:
    data = json.load(file)

#Update the data(Modify)
data["Exp"] = 6

#write to file
with open("C://Users//WINDOW 11//PycharmProjects//PythonAdvancedProgramming//Dataframes//writingfile.json",
          'w') as file:
    json.dump(data, file, indent = 4)
